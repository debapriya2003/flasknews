from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests

client = MongoClient("mongodb+srv://tintin:tintin@cluster0.qot4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.news_database
collection = db.news_articles

@app.route('/news', methods=['GET'])
def get_news():
    news_items = []
    for article in collection.find().sort('_id', -1):
        news_items.append({
            'image': article['image'],
            'headline': article['headline'],
            'description': article['description'],
            'adImage': article['adImage'],
            'link': article['link'],
        })
    return jsonify(news_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
