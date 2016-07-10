from django.contrib import admin

from .models import Loyer, HousingType, NumberOfRooms


admin.site.register(Loyer)
admin.site.register(HousingType)
admin.site.register(NumberOfRooms)