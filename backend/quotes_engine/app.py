from flask import Flask, request, jsonify
import random
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# Define categorized quotes
categorized_quotes = {
        'motivation': [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
        "Entrepreneurship is living a few years of your life like most people won't, so that you can spend the rest of your life like most people can't. - Unknown",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "It's not about ideas. It's about making ideas happen. - Scott Belsky"
    ],
    'happiness': [
        "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
        "The happiest people don't have the best of everything, they make the best of everything. - Unknown",
        "Happiness is not in the mere possession of money; it lies in the joy of achievement, in the thrill of creative effort. - Franklin D. Roosevelt",
        "Happiness is not by chance, but by choice. - Jim Rohn",
        "If you want to be happy, set a goal that commands your thoughts, liberates your energy, and inspires your hopes. - Andrew Carnegie",
        "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "Happiness is not having what you want. It is appreciating what you have. - Unknown"
    ],
    'success': [
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "Success is not in what you have, but who you are. - Bo Bennett",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "Success is not the destination, but the road that you're on. Being successful means that you're working hard and walking your walk every day. You can only live your dream by working hard towards it. That's living your dream. - Marlon Wayans",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
        "Success is not the absence of failure; it's the persistence through failure. - Aisha Tyler",
        "Success is not just about making money. It's about making a difference. - Unknown"
    ],
    'leadership': [
        "Leadership is not about being in charge. It is about taking care of those in your charge. - Simon Sinek",
        "Leadership is the capacity to translate vision into reality. - Warren Bennis",
        "Leadership is the art of getting someone else to do something you want done because he wants to do it. - Dwight D. Eisenhower",
        "The function of leadership is to produce more leaders, not more followers. - Ralph Nader",
        "A genuine leader is not a searcher for consensus but a molder of consensus. - Martin Luther King Jr.",
        "The greatest leader is not necessarily the one who does the greatest things. He is the one that gets the people to do the greatest things. - Ronald Reagan",
        "Leadership is the ability to guide others without force into a direction or decision that leaves them still feeling empowered and accomplished. - Lisa Cash Hanson",
        "A leader is one who knows the way, goes the way, and shows the way. - John C. Maxwell",
        "The art of leadership is saying no, not saying yes. It is very easy to say yes. - Tony Blair",
        "A leader is best when people barely know he exists, when his work is done, his aim fulfilled, they will say: we did it ourselves. - Lao Tzu"
    ],
    'creativity': [
        "Creativity is intelligence having fun. - Albert Einstein",
        "The secret of getting ahead is getting started. - Mark Twain",
        "You can't use up creativity. The more you use, the more you have. - Maya Angelou",
        "Creativity is piercing the mundane to find the marvelous. - Bill Moyers",
        "Every child is an artist. The problem is how to remain an artist once we grow up. - Pablo Picasso",
        "To live a creative life, we must lose our fear of being wrong. - Joseph Chilton Pearce",
        "Creativity is allowing yourself to make mistakes. Art is knowing which ones to keep. - Scott Adams",
        "The worst enemy to creativity is self-doubt. - Sylvia Plath",
        "Imagination is everything. It is the preview of life's coming attractions. - Albert Einstein",
        "The desire to create is one of the deepest yearnings of the human soul. - Dieter F. Uchtdorf"
    ],
    'doctor': [
        "The good physician treats the disease; the great physician treats the patient who has the disease. - William Osler",
        "To cure sometimes, to relieve often, to comfort always. - Hippocrates",
        "The art of medicine consists of amusing the patient while nature cures the disease. - Voltaire",
        "The greatest medicine of all is to teach people how not to need it. - Hippocrates",
        "Wherever the art of medicine is loved, there is also a love of humanity. - Hippocrates",
        "The doctor of the future will give no medicine but will interest his patients in the care of the human frame, in diet, and in the cause and prevention of disease. - Thomas Edison",
        "The doctor sees all the weakness of mankind, the lawyer all the wickedness, the theologian all the stupidity. - Arthur Schopenhauer",
        "It is not the healthy who need a doctor, but the sick. - Jesus Christ",
        "The best doctor gives the least medicines. - Benjamin Franklin",
        "The physician's high and only mission is to restore the sick to health, to cure, as it is termed. - Samuel Hahnemann"
    ],
    'lawyer': [
        "Lawyers are the foot soldiers of our Constitution. - Rennard Strickland",
        "The first duty of society is justice. - Alexander Hamilton",
        "Lawyers are operators of the toll bridge across which anyone in search of justice has to pass. - Jane Bryant Quinn",
        "The good lawyer is not the man who has an eye to every side and angle of contingency, and qualifies all his qualifications, but who throws himself on your part so heartily, that he can get you out of a scrape. - Ralph Waldo Emerson",
        "It is the trade of lawyers to question everything, yield nothing, and talk by the hour. - Thomas Jefferson",
        "The clearest way to show what the rule of law means to us in everyday life is to recall what has happened when there is no rule of law. - Dwight D. Eisenhower",
        "The law is reason, free from passion. - Aristotle",
        "It is better to be a mouse in a cat's mouth than a man in a lawyer's hands. - Spanish Proverb",
        "The first thing we do, let's kill all the lawyers. - William Shakespeare",
        "The only way to have a friend is to be one. - Ralph Waldo Emerson"
    ],
    'engineer': [
        "Engineering is the closest thing to magic that exists in the world. - Elon Musk",
        "The scientist discovers a new type of material or energy and the engineer discovers a new use for it. - Gordon Lindsay Glegg",
        "Engineers like to solve problems. If there are no problems handily available, they will create their own problems. - Scott Adams",
        "The ideal engineer is a composite... He is not a scientist, he is not a mathematician, he is not a sociologist or a writer; but he may use the knowledge and techniques of any or all of these disciplines in solving engineering problems. - Nathan W. Dougherty",
        "I am not a scientist. I am, rather, an engineer and a builder. - Herbert Hoover",
        "Engineers believe that if it ain't broke, it doesn't have enough features yet. - Scott Adams",
        "The engineer has been, and is, a maker of history. - James Kip Finch",
        "The engineer's first problem in any design situation is to discover what the problem really is. - Unknown",
        "The fewer moving parts, the better. - Ferdinand Porsche",
        "The engineer who builds engines and other machines ingeniously is seen as clever. The engineer who connects those engines to other people and communities is seen as wise. - Henry Petroski"
    ],
    'teacher': [
        "The mediocre teacher tells. The good teacher explains. The superior teacher demonstrates. The great teacher inspires. - William Arthur Ward",
        "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
        "A good teacher can inspire hope, ignite the imagination, and instill a love of learning. - Brad Henry",
        "Teaching is the profession that teaches all the other professions. - Unknown",
        "The art of teaching is the art of assisting discovery. - Mark Van Doren",
        "Teaching is not a lost art, but the regard for it is a lost tradition. - Jacques Barzun",
        "In learning, you will teach, and in teaching, you will learn. - Phil Collins",
        "The best teachers are those who show you where to look but don't tell you what to see. - Alexandra K. Trenfor",
        "The greatest sign of success for a teacher... is to be able to say, 'The children are now working as if I did not exist.' - Maria Montessori",
        "Teaching kids to count is fine, but teaching them what counts is best. - Bob Talbert"
    ],
    'artist': [
        "Every artist was first an amateur. - Ralph Waldo Emerson",
        "Art is the lie that enables us to realize the truth. - Pablo Picasso",
        "The purpose of art is washing the dust of daily life off our souls. - Pablo Picasso",
        "Art enables us to find ourselves and lose ourselves at the same time. - Thomas Merton",
        "The artist is nothing without the gift, but the gift is nothing without work. - Émile Zola",
        "Art is not what you see, but what you make others see. - Edgar Degas",
        "Every artist dips his brush in his own soul, and paints his own nature into his pictures. - Henry Ward Beecher",
        "To be an artist is to believe in life. - Henry Moore",
        "Art should comfort the disturbed and disturb the comfortable. - Banksy",
        "The world always seems brighter when you've just made something that wasn't there before. - Neil Gaiman"
    ]
}

# Dictionary to store used quotes for each category
used_quotes = {category: [] for category in categorized_quotes}

def generate_inspirational_quote(mood=None, preference=None, topic=None, tags=None):
    if mood:
        filtered_quotes = []
        for category, quotes in categorized_quotes.items():
            for quote in quotes:
                if mood.lower() in quote.lower():
                    filtered_quotes.append(quote)

        if not filtered_quotes:
            return None

        selected_quote = random.choice(filtered_quotes)

        for category, quotes in categorized_quotes.items():
            if selected_quote in quotes:
                used_quotes[category].append(selected_quote)
                break

        return selected_quote

    if preference:
        filtered_quotes = []
        for category, quotes in categorized_quotes.items():
            for quote in quotes:
                if preference.lower() in quote.lower():
                    filtered_quotes.append(quote)

        if not filtered_quotes:
            return None

        selected_quote = random.choice(filtered_quotes)

        for category, quotes in categorized_quotes.items():
            if selected_quote in quotes:
                used_quotes[category].append(selected_quote)
                break

        return selected_quote

    if topic:
        filtered_quotes = []
        for category, quotes in categorized_quotes.items():
            for quote in quotes:
                if topic.lower() in quote.lower():
                    filtered_quotes.append(quote)

        if not filtered_quotes:
            return None

        selected_quote = random.choice(filtered_quotes)

        for category, quotes in categorized_quotes.items():
            if selected_quote in quotes:
                used_quotes[category].append(selected_quote)
                break

        return selected_quote

    if tags:
        filtered_quotes = []
        for category, quotes in categorized_quotes.items():
            for quote in quotes:
                if tags.lower() in quote.lower():
                    filtered_quotes.append(quote)

        if not filtered_quotes:
            return None

        selected_quote = random.choice(filtered_quotes)

        for category, quotes in categorized_quotes.items():
            if selected_quote in quotes:
                used_quotes[category].append(selected_quote)
                break

        return selected_quote

    # If none of the filtering criteria are specified, return a random quote from all categories
    all_quotes = [quote for quotes in categorized_quotes.values() for quote in quotes]

    if not all_quotes:
        return None

    selected_quote = random.choice(all_quotes)

    for category, quotes in categorized_quotes.items():
        if selected_quote in quotes:
            used_quotes[category].append(selected_quote)
            break

    return selected_quote


@app.route('/inspirational_quote', methods=['GET'])
def get_inspirational_quote():
    # Extract query parameters from the request
    mood = request.args.get('mood')
    preference = request.args.get('preference')
    topic = request.args.get('topic')
    tags = request.args.get('tags')

    # Call the generate_inspirational_quote function with the provided parameters
    quote = generate_inspirational_quote(mood=mood, preference=preference, topic=topic, tags=tags)

    if quote:
        return jsonify({'quote': quote})
    else:
        return jsonify({'error': 'No matching quotes found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
