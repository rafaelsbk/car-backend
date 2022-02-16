from django.shortcuts import render
from rest_framework import viewsets

from car.models import Car
from car.serializers import CarSerializer

# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
