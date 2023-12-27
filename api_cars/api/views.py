from rest_framework import viewsets, filters
from api.models import Car, Rate
from api.serializers import CarSerializer, RateSerializer, PopularSerializer
from django.db.models import Avg, Count


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().annotate(
        avg_rating=Avg('rate__rating'))
    serializer_class = CarSerializer
    filter_backends = (filters.OrderingFilter,)


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class PopularViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().annotate(
        rates_number=Count('rate__rating'))
    serializer_class = PopularSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-rates_number',)
