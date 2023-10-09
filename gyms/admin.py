from django.contrib import admin
from .models import Gym, Amenity

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price_per_night",
        "owner"
    )

    list_filter = (
        "country",
        "city",
        "price_per_night"
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at"
    )
