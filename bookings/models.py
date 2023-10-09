from django.db import models
from common.models import CommonModel

class Booking(CommonModel):

    description = models.TextField(max_length=300)
    membership = models.ForeignKey("memberships.Membership", on_delete=models.CASCADE)

    candidate_times = models.ManyToManyField("bookings.CandidateTime", blank=True)

    complete = models.BooleanField(default=False)

class CandidateTime(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()