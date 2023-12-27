from django.core.validators import (MinValueValidator, MaxValueValidator)
from django.db import models


class Car(models.Model):
    make = models.CharField('Марка автомобиля', max_length=256)
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
        error_messages={'validators': 'Оценка от 1 до 5!'}
    )


class Popular(models.Model):
    car_id = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='popular',
        verbose_name='ID автомобиля'
        )
    rates_number = models.ForeignKey(
        Rate,
        on_delete=models.CASCADE,
        related_name='popular',
        verbose_name='Рейтинг')