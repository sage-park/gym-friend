from django.db import models

# Create your models here.

class Gym(models.Model):

    """Modle Definition for Gym"""

    name= models.CharField(max_length=140)
    description = models.TextField()
    address = models.CharField(max_length=140)