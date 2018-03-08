from flask import Flask, render_template, jsonify, redirect
from pymongo import MongoClient
from key import *
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient(moClient)
db = client[dbClient]

# Convert MongoDB to JSON
def to_json(data):
    return dumps(data)

@app.route('/')
def index():
	
	return "Hello world"

#Add thing to db as W3C standard
@app.route('/add')
def add_to_db():

        initial_things = [{
                        "@context": ["http://w3c.github.io/wot/w3c-wot-td-context.jsonld"],
                        "@type": ["Thing"],
                        "name": "MyLampThing",
                                "interaction": [
                        {
                                                "@type": ["Property"],
                                                "name": "status",
                                                "outputData": {"type": "string"},
                                                "writable": 'false',
                                                "link": [{
                                                        "href": "coaps://mylamp.example.com:5683/status",
                                                        "mediaType": "application/json"
                                                        }]
                        }
        ]}]
        result = db.dbClient.insert_many(initial_things)
        print result.inserted_ids
	return "added"
#show thing collection as Json
@app.route('/things/', methods=['GET'])
def get_thing():
	# Get the thing collection
        things_collection = db.dbClient.find()
    # Create JSON-data from collection via a Python list
        things_list = list(things_collection)
        things = dumps(things_list)
        return things


if __name__ == '__main__':
    app.run(host='0.0.0.0')
