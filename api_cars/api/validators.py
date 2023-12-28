from django.core.exceptions import ValidationError
import requests
import json

response = requests.get(
    'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json')
obj = response.json()
result = json.dumps(obj)


def validate_car(make):
    """Проверка существования автомобиля
    на сайте https://vpic.nhtsa.dot.gov/api/"""
    if make not in result.split('"'):
        raise ValidationError(
            'Такого автомобиля не существует!\
            Проверьте корректность ввода данных.\
            Используйте только английские заглавные буквы!',
            params={'make': make},
        )
