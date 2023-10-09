from django.contrib import admin
from .models import Gym, Amenity

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    pass

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
