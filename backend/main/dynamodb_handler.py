from boto3 import client, resource
from decouple import config

AWS_ACCESS_KEY_ID     = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME           = config("REGION_NAME")

client = client(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)

resource = resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)

def create_user_profiles_table():
    client.create_table(
        AttributeDefinitions = [
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            }
        ],
        TableName = 'UserProfiles', # Name of the table 
        KeySchema = [       # 
            {
                'AttributeName': 'username',
                'KeyType'      : 'HASH' # HASH -> partition key, RANGE -> sort key
            }
        ],
        BillingMode = 'PAY_PER_REQUEST'
    )

def create_inspirational_quotes_table():
    client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'quote_id',
                'AttributeType': 'N'
            }
        ],
        TableName='InspirationalQuotes',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'quote_id',
                'KeyType': 'RANGE'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

def add_user_profile(username, profession, followers):
    try:
        table = resource.Table('UserProfiles')
        response = table.put_item(
            Item={
                'username': username,
                'profession': profession,
                'followers': followers
            }
        )
        return response
    except Exception as e:
        return {'error': str(e)}
    
def increase_followers(email):
    try:
        table = resource.Table('UserProfiles')
        response = table.update_item(
            Key={'email': email},
            UpdateExpression='SET followers = followers + :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues='UPDATED_NEW'
        )
        return response
    except Exception as e:
        return {'error': str(e)}

def add_quote(username, quote_text):
    try:
        table = resource.Table('InspirationalQuotes')
        # Query DynamoDB to find the maximum quote_id
        response = table.scan(
            Select='COUNT',  # Get the count of items
            FilterExpression='username = :username',  # Filter by username
            ExpressionAttributeValues={
                ':username': username
            }
        )
        max_quote_id = response['Count'] + 1  # Increment by 1 to get the next available quote_id
        response = table.put_item(
            Item={
                'username': username,
                'quote_id': max_quote_id,
                'quote_text': quote_text,
                'likes': 0,
                'dislikes': 0
            }
        )
        return response
    except Exception as e:
        return {'error': str(e)}
    
def update_quote_like(username, quote_id):
    try:
        table = resource.Table('InspirationalQuotes')
        # Query DynamoDB to find the maximum quote_id
        response = table.scan(
            Select='COUNT',  # Get the count of items
            FilterExpression='username = :username',  # Filter by username
            ExpressionAttributeValues={
                ':username': username
            }
        )
        # Retrieve the quote from the DynamoDB table
        response = table.get_item(
            Key={
                'username': username,
                'quote_id': quote_id
            }
        )
        quote_item = response.get('Item')

        if quote_item:
            # Increment the like count
            likes = quote_item.get('likes', 0) + 1

            # Update the quote item in the table with the incremented like count
            table.update_item(
                Key={
                    'username': username,
                    'quote_id': quote_id
                },
                UpdateExpression='SET likes = :likes',
                ExpressionAttributeValues={':likes': likes}
            )

        return response
    except Exception as e:
        return {'error': str(e)}

def get_quotes(username):
    try:
        table = resource.Table('InspirationalQuotes')
        # Query DynamoDB to get quotes for the specified username
        response = table.scan(
            FilterExpression='username = :username',
            ExpressionAttributeValues={
                ':username': username
            }
        )
        quotes = response.get('Items', [])
        return quotes
    except Exception as e:
        return {'error': str(e)}
    

def GetUser(username):
    response = resource.Table('UserProfiles').get_item(
        Key = {
            'username'     : username
        },
        AttributesToGet=[
            'email' # valid types dont throw error, 
                              # Other types should be converted to python type before sending as json response
        ]
    )
    return response
