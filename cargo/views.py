from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import CargoSerializer
from .models import CargoModel
from truck.models import TruckModel


class CargoView(ModelViewSet):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer


class Test(ReadOnlyModelViewSet):

    f = TruckModel.objects.values_list('lat', 'lng')





