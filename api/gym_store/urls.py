from django.urls import path

from . import apis

urlpatterns = [
    path('store/', apis.ProductListAPI.as_view()),
    path('store/<int:pk>/', apis.ProductDetailAPI.as_view()),
    path('pass/', apis.PassListAPI.as_view()),
]
