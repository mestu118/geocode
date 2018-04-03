#Created by: Mark J. Estudillo
#Created on Monday, April 2nd, 2018
#Last Modified: April 2nd, 2018
#Execute: python requesting.py (Location)
#BuzzFeed TakeHome test.
import requests
import sys

#API_KEY to be able to make the request
api_key = 'AIzaSyAqPaARrA5KGrSfkfhtdxdqKT8Bl-exNek'

#The location that is inputted by the user
location = sys.argv[1]

#Payload that will be used for the parameters in the json request
payload = {'address' : location, 'key' : api_key}

#Request is made and converted to a JSON object.
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json' , params = payload)
r = r.json()

#Obtaining the results from the JSON object obtained
Results = r.get('results')

#Getting the long name
longName = (Results[0]).get('address_components')[0].get('long_name')

#Getting the place_id
ID = (Results[0]).get('place_id')

#Lattiude and Longitude
Latitude = (Results[0]).get('geometry').get('location').get('lat')
Longitude  = (Results[0]).get('geometry').get('location').get('lng')

#Printing out the request fields
print(longName)
print("ID: " + ID)
print("Latitude: " + str(Latitude))
print("Longitude: " + str(Longitude)