from .models import TruckModel
from rest_framework import serializers


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckModel
        fields = '__all__'