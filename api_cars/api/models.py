from django.core.validators import (MinValueValidator, MaxValueValidator)
from django.db import models
from api.validators import validate_car


class Car(models.Model):
    make = models.CharField(
        'Марка автомобиля',
        max_length=256,
        validators=[validate_car])
    model = models.CharField('Модель автомобиля', max_length=256)


class Rate(models.Model):
    car_id = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='rate',
        verbose_name='ID автомобиля')
    rating = models.PositiveIntegerField(
        'оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(5),
        ),
    )
