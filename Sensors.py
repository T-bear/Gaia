#This code lets a sensor connected to a Raspberry Pi 3 to send data to a mongodb client.
#To use your own database put in your client and db and change collection name.
#!/usr/bin/python

from flask import Flask
import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import smtplib # This is the SMTP library we need to send the email notification
import time # This is the time library, we need this so we can use the sleep function
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError
from bson.objectid import ObjectId

client = ""
db = ""

#database client and db.
try:
    client = MongoClient('155.4.72.38', 27017)
    db = client['pangaea']
except ConnectionFailure, ConfigurationError:
    print "Uppkopplingsfel"
except ConfigurationError:
    print "Fel user/server-uppgifter"

#---------------------------------------------------Moisture Sensor----------------------------------------------------------------------------
#db.<collection name>.update
def moistureSensor(channel):
        if GPIO.input(channel):
            #update db when sensor send new event.
                data = db.greenhous.update({"_id": ObjectId("5b07c63274fece7f5b506a4d")}, {"$set": {"humiditysensor": "Behöver inte vattnas"}})
        else:
                data = db.greenhous.update({"_id": ObjectId("5b07c63274fece7f5b506a4d")}, {"$set": {"humiditysensor": "Behöver vattnas"}})

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, moistureSensor)

# This is an infinte loop to keep our script running
while True:
        # This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
        time.sleep(0.1)
#---------------------------------------------------Moisture Sensor----------------------------------------------------------------------------

