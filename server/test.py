from flask import  Flask, render_template, jsonify, redirect
from pymongo import MongoClient
#from key import *
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient('localhost')
db = client['pangaea']

# Convert MongoDB to JSON
def to_json(data):
    return dumps(data)

@app.route('/')
def index():
	
	return "Hello world"

#Add thing to db as W3C standard
@app.route('/add')
def add_to_db():

        initial_things = {
    			"@context": ["https://tillsammansodling/karlshamn/bth/gaia"],
    			"@type": ["vaxthus"],
    			"name": "gaia",
    			"city": "Karlshamn",
    			"location": "bth",
    			"interaction": [{
        			"@type": [{"lightsensor": "1",
                  			"humiditysesnor": "2",
                  			"moisturesensor": "3"}],
        			"name": "status",
        			"schema": {"tpye": "string"},
        			"writable": False,
        			"observable": True,
        			"form": [{
            				"href": "tillsammansodling/karlshamn/gaia/status",
            				"mediaType": "application/json"
        				}]
    				}]
			}
        result = db.greenhous.insert_one(initial_things)
        #print result.inserted_ids
	return "added"
#show thing collection as Json
@app.route('/things/', methods=['GET'])
def get_thing():
	# Get the thing collection
        things_collection = db.greenhous.find()
    # Create JSON-data from collection via a Python list
        things_list = list(things_collection)
        things = dumps(things_list)
        return things

@app.route('/test', methods=['GET'])
def get_sensor_data():


        # Get the thing collection
        things_collection = db.greenhous.find()
    # Create JSON-data from collection via a Python list
        things_list = list(things_collection)
        things = dumps(things_list)
	for name in things_list:
		print (name)
        return "yolo"

@app.route('/<city>/<location>/<name>/', methods=['GET'])
def greenhouse(city, location, name):
	things_collection = db.greenhous.find()

	things_list = list(things_collection)

	for x in things_list:
		city = city
		location = location
		name = name

	return "X" #render_template('vaxthus.html', things_list=things_list)

@app.route('/star/', methods=['GET'])
def get_one_star(name):
  star = mongo.pangaea.greenhous
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['name']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
