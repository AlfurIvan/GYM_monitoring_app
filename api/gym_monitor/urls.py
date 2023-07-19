from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "gym_monitor"
urlpatterns = [
    path('', views.index),
]


urlpatterns = format_suffix_patterns(urlpatterns)
