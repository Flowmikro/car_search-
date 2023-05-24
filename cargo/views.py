from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import CargoSerializer
from .models import CargoModeTEstTEst
from truck.models import TruckModel


class CargoView(ModelViewSet):
    queryset = CargoModeTEstTEst.objects.all()
    serializer_class = CargoSerializer



