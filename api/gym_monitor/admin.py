from django.contrib import admin

from .models import News, NewsComment, TrainingProgram

admin.site.register(News)
admin.site.register(NewsComment)
admin.site.register(TrainingProgram)
