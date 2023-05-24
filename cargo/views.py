from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import CargoSerializer
from .models import CargoModeTEstTEst


class CargoView(ModelViewSet):
    queryset = CargoModeTEstTEst.objects.all()
    serializer_class = CargoSerializer
