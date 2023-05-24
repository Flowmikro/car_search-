from .models import CargoModeTEstTEst
from rest_framework import serializers


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModeTEstTEst
        fields = '__all__'