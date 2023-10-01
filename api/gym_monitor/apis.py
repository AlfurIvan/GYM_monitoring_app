from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework import views, response, exceptions, permissions

from . import models as monitor_models
from . import serializer as monitor_serializer
from user import authentication


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
    GET: Retrieve list of News with related objects
    """
    queryset = monitor_models.News.objects.prefetch_related(None)
    serializer_class = monitor_serializer.NewsSerializer


class NewsDetail(views.APIView):
    """
    GET:  Retrieve News record with related
        comments & comments.author(User).
    """

    def get(self, request, pk):
        try:
            news_obj = (monitor_models.News.objects
                        .prefetch_related("comments")
                        .get(id=pk))
            serializer = monitor_serializer.NewsSerializer(news_obj)
            return response.Response(serializer.data)
        except monitor_models.News.DoesNotExist:
            return response.Response({"error": "There is no record with this ID 0_o"})


class CommentCreate(views.APIView):
    """
    POST: Creates new comment(attached to News with id=pk)
        if user isn`t AnonymousUser & body is valid
    """
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        author = request.user
        if isinstance(author, AnonymousUser):
            raise PermissionDenied()

        try:
            body = request.data['body']
        except KeyError:
            return response.Response(data={'error':'Incorrect input'})
        else:

            pub_date = datetime.now()
            attached_to = monitor_models.News.objects.get(id=pk)
            instance = monitor_models.NewsComment(
                attached_to=attached_to,
                body=body,
                pub_date=pub_date,
                author=author,
            )
            instance.save()

            return response.Response(data=monitor_serializer.NewsSerializer(attached_to).data)


class TrainingProgramList(generics.ListAPIView):
    """
    GET: Retrieve list of TrainingProgram-s
    """
    queryset = monitor_models.TrainingProgram.objects.all()
    serializer_class = monitor_serializer.TrainingProgramSerializer


class TrainingProgramDetail(generics.RetrieveAPIView):
    """
    GET: Retrieve specific TrainingProgram
    """
    queryset = monitor_models.TrainingProgram.objects.all()
    serializer_class = monitor_serializer.TrainingProgramSerializer
