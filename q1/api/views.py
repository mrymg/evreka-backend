from datetime import datetime, timedelta

from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from q1.api.serializers import NavigationRecordSerializer, VehicleSerializer
from q1.models import NavigationRecord, Vehicle


class NavigationRecordListAPIView(ListAPIView):
    serializer_class = NavigationRecordSerializer

    def get_queryset(self):
        today = datetime.now()
        timeDif = today - timedelta(days=2)  # should be 2 days
        return NavigationRecord.objects.filter(Q(datetime__gte=timeDif))

class NavigationRecordAPIView(RetrieveAPIView):
    serializer_class = NavigationRecordSerializer
    queryset = NavigationRecord.objects.all()
    lookup_field = 'pk'

class VehicleListAPIView(ListAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleAPIView(RetrieveAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = 'pk'

class addVehicle(CreateAPIView):
    serializer_class = VehicleSerializer

class addRecord(CreateAPIView):
    serializer_class = NavigationRecordSerializer