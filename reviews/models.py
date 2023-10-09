from django.db import models
from common.models import CommonModel

class Review(CommonModel):

    writer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE,

    )

    gym = models.ForeignKey(
        "gyms.Gym", on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews"
    )

    content = models.TextField()
    rating = models.PositiveIntegerField()



