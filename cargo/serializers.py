from .models import CargoModel
from rest_framework import serializers


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModel
        fields = '__all__'