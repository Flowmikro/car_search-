from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from geopy.distance import geodesic as GD
from .serializers import CargoSerializer
from .models import CargoModel
from truck.models import TruckModel


class CargoView(ModelViewSet):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Получаем все грузы, которые еще не были забраны и у которых есть координаты
        unpicked_cargos = queryset.filter(pick_up=True).exclude(lat_pick_up=True)

        # Получаем все грузовики, у которых есть координаты
        trucks = TruckModel.objects.exclude(lat=None).exclude(lng=None)

        result = []

        for cargo in unpicked_cargos:
            cargo_location = (cargo.lat_pick_up, cargo.lng_pick_up)
            nearby_trucks_count = 0

            for truck in trucks:
                truck_location = (truck.lat, truck.lng)
                distance = GD(cargo_location, truck_location).miles

                if distance <= 450:
                    nearby_trucks_count += 1

            result.append({
                'cargo': CargoSerializer(cargo).data,
                'nearby_trucks_count': nearby_trucks_count
            })

        return Response(result)






