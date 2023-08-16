from rest_framework import views, response, exceptions, permissions
from rest_framework import generics

from . import models as store_models
from . import serializer as store_serializer


class PassListAPI(views.APIView):
    def get(self, request):
        pass_representation = {
            "passes": [
                {
                    "price": "600",
                    "month_to_expire": "1"
                },
                {
                    "price": "1100",
                    "month_to_expire": "2"
                },
                {
                    "price": "1500",
                    "month_to_expire": "3"
                }
            ]
        }
        return response.Response(data=pass_representation)


class ProductListAPI(generics.ListAPIView):
    queryset = store_models.Product.objects.all()
    serializer_class = store_serializer.ProductSerializer


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = store_models.Product.objects.all()
    serializer_class = store_serializer.ProductSerializer
