from django.db import models

class Membership(models.Model):

    start = models.DateField()
    end = models.DateField()

    gym = models.ForeignKey("gyms.Gym", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

