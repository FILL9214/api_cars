from rest_framework import serializers
from api.models import Car, Rate


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор списка автомобилей со средней оценкой"""
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = ('id', 'make', 'model', 'avg_rating')
        model = Car


class RateSerializer(serializers.ModelSerializer):
    """Сериализатор рейтинга автомобилей"""
    class Meta:
        fields = ('id', 'car_id', 'rating')
        model = Rate


class PopularSerializer(serializers.ModelSerializer):
    """Сериализатор популярных автомобилей на основании оценок"""
    rates_number = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'make', 'model', 'rates_number')
        model = Car
        ordering = ('rates_number')
