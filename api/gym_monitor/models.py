from django.utils import timezone
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2048)
    pub_date = models.DateTimeField('date_published')
    # image = models.ImageField(default=None)


class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2048)
    tags = models.CharField(max_length=255)
    # image = models.ImageField(default=None)
    # trainers 
