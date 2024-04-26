from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)

import dynamodb_handler as dynamodb

CORS(app)  # Enable CORS for all routes in the Flask app

@app.route('/create_user_profiles_table')
def table_create_route1():
    dynamodb.create_user_profiles_table()
    return 'Table Created'

@app.route('/create_inspirational_quotes_table')
def table_create_route2():
    dynamodb.create_inspirational_quotes_table()
    return 'Table Created'

@app.route('/add_user_profile', methods=['POST'])
def add_user_profile_data():
    data = request.get_json()
    response = dynamodb.add_user_profile(data['username'], data['profession'], followers=0)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }
    return {  
        'msg': 'Some error occcured',
        'response': response
    }


@app.route('/increase_followers', methods=['POST'])
def increase_followers_route():
    data = request.json
    email = data.get('email')
    response = dynamodb.increase_followers(email)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Followed successfully',
        }
    return {  
        'msg': 'Some error occcured',
        'response': response
    }


@app.route('/add_quote', methods=['POST'])
def add_quote_route():
    data = request.json
    username = data.get('username')
    quote_text = data.get('quote')
    response = dynamodb.add_quote(username, quote_text)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }
    return {  
        'msg': 'Some error occcured',
        'response': response
    }

@app.route('/get_quotes', methods=['POST'])
def get_quotes_route():
    data = request.json
    username = data.get('username')
    quotes = dynamodb.get_quotes(username)
    if isinstance(quotes, list):
        return {
            'msg': 'Quotes retrieved successfully',
            'quotes': quotes
        }
    return {  
        'msg': 'Some error occurred',
        'error': quotes.get('error')
    }

@app.route('/like_quote', methods=['POST'])
def like_quote():
    data = request.json
    username = data.get('username')
    quote_id = data.get('quote_id')
    response = dynamodb.update_quote_like(username, quote_id)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'updated successfully',
        }
    return {  
        'msg': 'Some error occcured',
        'response': response
    }


@app.route('/check_username/<string:username>', methods=['GET'])
def getuser(username):
    response = dynamodb.GetUser(username)
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        
        if ('Item' in response):
            return { 'Item': response }

        return { 'msg' : 'Item not found!' }

    return {
        'msg': 'Some error occured',
        'response': response
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)