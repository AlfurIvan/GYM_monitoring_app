from datetime import datetime
from django.http import JsonResponse
from rest_framework import generics

from . import models
from . import serializer


def date_and_time(request):
    current_time = datetime.now().strftime("%-I:%M %p")
    current_date = datetime.now().strftime("%A %m %-Y")

    data = {
        'time': current_time,
        'date': current_date,
    }

    return JsonResponse(data)


class NewsList(generics.ListAPIView):
    """
    """
    queryset = models.News.objects.all()
    serializer_class = serializer.NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = models.News.objects.all()
    serializer_class = serializer.NewsSerializer


class TrainingProgramList(generics.ListAPIView):
    queryset = models.TrainingProgram.objects.all()
    serializer_class = serializer.TrainingProgramSerializer


class TrainingProgramDetail(generics.RetrieveAPIView):
    queryset = models.TrainingProgram.objects.all()
    serializer_class = serializer.TrainingProgramSerializer
