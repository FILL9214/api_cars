from rest_framework import routers
from api.views import CarViewSet, RateViewSet, PopularViewSet
router = routers.DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'rate', RateViewSet, basename='rate')
router.register(r'popular', PopularViewSet, basename='popular')
