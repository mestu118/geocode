import requests
import sys

api_key = 'AIzaSyAqPaARrA5KGrSfkfhtdxdqKT8Bl-exNek'
location = sys.argv[1]
payload = {'address':location, 'key':api_key}
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json' , params = payload)
print(r.json())
