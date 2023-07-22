from django.utils import timezone
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date_published')
    # image = models.ImageField(default=None)


# class Gym(models.Model):
#     address = models.CharField(max_length=150)
#     description = models.CharField(max_length=300)
#     # equipment
#     # pictures
