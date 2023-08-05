from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "gym_monitor"
urlpatterns = [
    path('dt/', views.date_and_time),
    path('', views.NewsList.as_view()),
    path('<int:pk>/', views.NewsDetail.as_view()),
    # path()
]

urlpatterns = format_suffix_patterns(urlpatterns)
