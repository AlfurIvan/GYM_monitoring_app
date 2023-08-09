from rest_framework import serializers

from user import serializer as user_serializer

from . import services


class PassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.IntegerField(required=True)
    month_to_expire = serializers.IntegerField(required=True)
    date_released = serializers.DateTimeField()
    user = user_serializer.UserSerializer(read_only=True)
    staff_who_released = user_serializer.UserSerializer(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.PassDataClass(**data)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=2048, required=True)
    manufacturer = serializers.CharField(max_length=255, required=True)
    price = serializers.IntegerField(required=True)
    amount = serializers.IntegerField(required=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.ProductDataClass(**data)
