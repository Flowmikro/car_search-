from rest_framework.viewsets import ModelViewSet

from .serializers import TruckSerializer
from .models import TruckModel


class TruckView(ModelViewSet):
    queryset = TruckModel.objects.all()
    serializer_class = TruckSerializer
