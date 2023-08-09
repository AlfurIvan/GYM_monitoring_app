from django.http import JsonResponse
from datetime import datetime

from rest_framework import generics

from .models import News
from .serializer import NewsSerializer


def date_and_time(request):
    current_time = datetime.now().strftime("%-I:%M %p")
    current_date = datetime.now().strftime("%A %m %-Y")

    data = {
        'time': current_time,
        'date': current_date,
    }

    return JsonResponse(data)


class NewsList(generics.ListCreateAPIView):
    """
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
