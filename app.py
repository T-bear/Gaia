from flask import  Flask, render_template, jsonify, redirect
from pymongo import MongoClient
from bson.json_util import dumps
import json

app = Flask(__name__)
client = MongoClient('localhost')
db = client['pangaea']


# Convert MongoDB to JSON
def to_json(data):
    return dumps(data)


@app.route('/')
def index():
    greenhouses = db.greenhouse.find()
    greenhouses_list = list(greenhouses)
    houses = dumps(greenhouses_list)
    return render_template('index.html', houses = greenhouses_list)

#Add thing to db as W3C standard
@app.route('/add')
def add_to_db():

        initial_things = {
                            ({"$oid": "5b07c63274fece7f5b506a4d",
                            "interaction": {
                            "humiditysensor": "FUNKAR DETTA ELLER!?"
                                        }
                             })
			             }
        result = db.greenhouse.update_one(initial_things)
        #print result.inserted_ids
	return "added"

#show thing collection as Json
@app.route('/things/', methods=['GET'])
def get_thing():
	# Get the thing collection
        things_collection = db.greenhouse.find()
    # Create JSON-data from collection via a Python list
        things_list = list(things_collection)
        things = dumps(things_list)
        return things

@app.route('/<city>/', methods=['GET'])
def get_city(city):
    city = db.greenhouse.find({"city": city})
    if city.count() <= 0:
        return "No city found"

    city_list = list(city)
    cityData = dumps(city_list)
    return render_template('vaxthus.html', cityData = city_list)

@app.route('/<city>/<location>/<name>/', methods=['GET'])
def get_url(city, location, name):
    url = db.greenhouse.find({"$and": [{"city": city, "location": location, "name": name}]})
    if url.count() <= 0:
        return "no url found"

    url_list = list(city)
    urlData = dumps(url_list)
    return render_template('ny.html', urlData = url_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
