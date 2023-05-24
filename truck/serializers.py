from rest_framework import serializers

from .models import TruckModel


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckModel
        fields = '__all__'