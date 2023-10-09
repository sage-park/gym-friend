from django.db import models

# Create your models here.

class Gym(models.Model):

    """Modle Definition for Gym"""

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")

    name= models.CharField(max_length=140)
    description = models.TextField()
    address = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Amenity(models.Model):

    """ Amenity Definition """

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)
