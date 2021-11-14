from django.db import models

# Create your models here.
class Vehicle(models.Model):
    plate = models.CharField(max_length=10, verbose_name="plate")
    def __str__(self):
        return self.plate
class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle', verbose_name= "Plate")
    lat = models.FloatField(default=0, verbose_name="Latitude")
    lng = models.FloatField(default=0, verbose_name="Longtitude")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Datetime")

    def __str__(self):
        return self.vehicle.plate