import requests
import json

response = requests.get(
    'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json')
obj = response.json()
result = json.dumps(obj)


def validate_car(make):
    if make in result:
        print(make)
    else:
        print('err')
