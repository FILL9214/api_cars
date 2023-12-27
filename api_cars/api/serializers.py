from rest_framework import serializers
from api.models import Car, Rate


class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = ('id', 'make', 'model', 'avg_rating')
        model = Car


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'car_id', 'rating')
        model = Rate


class PopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'make', 'model', 'rates_number')
        model = Car
        ordering = ('rates_number')
