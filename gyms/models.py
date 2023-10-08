from django.db import models

# Create your models here.

class Gym(models.Model):

    """Modle Definition for Gym"""

    name= models.CharField(max_length=140)
    description = models.TextField()
    address = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name