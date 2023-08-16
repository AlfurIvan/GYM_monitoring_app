from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2048)
    pub_date = models.DateTimeField('date_published')
    # image = models.ImageField(default=None)


# class NewsComment(models.Model):
#     body = models.CharField(max_length=255)
#     pub_date = models.DateTimeField('date_published')
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET(None),
#         verbose_name="User",
#         related_name="comments"
#     )
#


class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2048)
    tags = models.CharField(max_length=255)
    # image = models.ImageField(default=None)
    # trainers
