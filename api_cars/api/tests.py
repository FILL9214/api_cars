import requests
from pprint import pprint

response = requests.get(
    'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json')
cars = response.json()
pprint(cars)


def validator(make: str):
    result = [x for x in cars if make in x["Make_Name"]]
    print(result)


validator("bmw")
