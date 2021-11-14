from django.contrib import admin

# Register your models here.
from q1.models import Vehicle, NavigationRecord

admin.site.register(Vehicle)
admin.site.register(NavigationRecord)