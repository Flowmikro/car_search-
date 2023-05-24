from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import CargoSerializer
from .models import CargoModel


class CargoView(ModelViewSet):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer
