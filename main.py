import os
from flask import Flask, jsonify
from pymongo import MongoClient

cluster = MongoClient(os.environ.get("DATABASE_URL"))
db = cluster['Travel']
collection = db['Places']

app = Flask(__name__)


@app.route('/getAllPlaces')
def home():
    return jsonify(list(collection.find({})))


if __name__ == '__main__':
    app.run(debug=True)
