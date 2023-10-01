from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import apis

app_name = "gym_monitor"
urlpatterns = [
    path('dt/', apis.date_and_time),
    path('', apis.NewsList.as_view()),
    path('<int:pk>/', apis.NewsDetail.as_view()),
    path('<int:pk>/new', apis.CommentCreate.as_view()),
    path('programs/', apis.TrainingProgramList.as_view()),
    path('programs/<int:pk>/', apis.TrainingProgramDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
