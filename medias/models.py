from django.db import models
from common.models import CommonModel

class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(max_length=140,)

