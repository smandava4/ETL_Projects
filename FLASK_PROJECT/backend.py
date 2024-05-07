from flask import Flask, request, jsonify, render_template
import tweepy
import config as c

app = Flask(__name__, static_folder='static')

# Initialize the Tweepy client
client = tweepy.Client(bearer_token=c.bearer_token,
                        access_token=c.access_token,
                        access_token_secret=c.access_token_secret,
                        consumer_key=c.api_key,
                        consumer_secret=c.api_secret)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_info', methods=['GET'])
def get_user_info():
    # Fetch user information
    user = client.get_me()
    user_data = {
        "name": user.name,
        "created_at": user.created_at,
        "description": user.description,
        # Add other user fields as needed
    }
    return jsonify(user_data)

@app.route('/post_tweet', methods=['POST'])
def post_tweet():
    tweet_text = request.json.get('tweet_text')
    response = client.create_tweet(text=tweet_text)
    
    # Check if the response is successful
    if response.data and 'id' in response.data:
        tweet_id = response.data['id']
        return jsonify({"tweet_id": tweet_id, "message": "Tweet posted successfully"}), 200
    else:
        # If there are errors in the response, return them
        if response.errors:
            return jsonify({"error": response.errors}), 400
        else:
            return jsonify({"error": "Unknown error occurred while posting tweet"}), 500


@app.route('/delete_tweet/<tweet_id>', methods=['DELETE'])
def delete_tweet(tweet_id):
    response = client.delete_tweet(tweet_id)
    if response.errors:
        return jsonify({"error": response.errors}), 400
    return jsonify({"message": "Tweet deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
