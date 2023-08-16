from django.contrib import admin
from django.urls import path

from cargo.views import CargoAPIList, CargoAPIDetail, CargoAPIUpdate
from truck.views import TruckAPIList, TruckAPIUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cargo/', CargoAPIList.as_view()),
    path('api/cargo/<int:pk>/', CargoAPIDetail.as_view()),
    path('api/cargo/update/<int:pk>/', CargoAPIUpdate.as_view()),

    path('api/truck/', TruckAPIList.as_view()),
    path('api/truck/<int:pk>/', TruckAPIUpdate.as_view()),
]
