import requests
import json

r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=68606/year=2019')
data = json.loads(r.text)
for stat in data['indicator_value']:
    print(stat)