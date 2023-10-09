from django.db import models
from common.models import CommonModel

class Gym(CommonModel):

    """Modle Definition for Gym"""

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")

    name= models.CharField(max_length=140)
    description = models.TextField()
    address = models.CharField(max_length=140)

    price_per_night = models.PositiveBigIntegerField(null=True)
    price_per_month = models.PositiveIntegerField(null=True)
    price_per_Three_month = models.PositiveIntegerField(null=True)
    price_per_Six_month = models.PositiveIntegerField(null=True)
    price_per_year = models.PositiveBigIntegerField(null=True)

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)

    amenities = models.ManyToManyField("gyms.Amenity", blank=True)

    def __str__(self):
        return self.name

class Amenity(CommonModel):

    """ Amenity Definition """

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"

    
