from flask import Flask, render_template, jsonify, redirect
from pymongo import MongoClient
from key import *

app = Flask(__name__)

client = MongoClient(moClient)
db = client[dbClient]

@app.route("/")
def hello():
	
	initial_things = [{
  			"@context": ["http://w3c.github.io/wot/w3c-wot-td-context.jsonld"],
  			"@type": ["Thing"],
  			"name": "MyLampThing",
  				"interaction": [
      			{
          					"@type": ["Property"],
          					"name": "status",
          					"outputData": {"type": "string"},
          					"writable": false,
          					"link": [{
              						"href": "coaps://mylamp.example.com:5683/status",
              						"mediaType": "application/json"
          						}]
      			}			
	]
	#initial_things = mongo.db.data
	#initial_things.insert({'Data': initial_things})
	#result = db.python-test.insert_many(initial_things)
	#print result.inserted_ids
if __name__ == '__main__':
    app.run(host='0.0.0.0')

