from django.urls import path, include

from q1 import views
from q1.api.views import NavigationRecordListAPIView, VehicleListAPIView, VehicleAPIView, NavigationRecordAPIView, addVehicle, addRecord

urlpatterns = [
    path('VehicleList', VehicleListAPIView.as_view(), name="VehicleList"),
    path('NavigationRecordList', NavigationRecordListAPIView.as_view(), name="NavigationRecordList"),
    path('NavigationRecord/<pk>', NavigationRecordAPIView.as_view(), name="detail"),
    path('vehicle/<pk>', VehicleAPIView.as_view(), name="detail"),
    path('create/vehicle', addVehicle.as_view(), name="create"),
    path('create/record', addRecord.as_view(), name="create")
]