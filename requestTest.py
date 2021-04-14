import requests
import json

r = requests.get('https://unstats.un.org/SDGAPI/v1/sdg/GeoArea/List')
dataGeo = json.loads(r.text)
for geo in dataGeo:
    print(geo['geoAreaName'])

r = requests.get('https://unstats.un.org/SDGAPI/v1/sdg/Goal/List?includechildren=true')
dataGoals = json.loads(r.text)
for goal in dataGoals:
    print(goal['title'])