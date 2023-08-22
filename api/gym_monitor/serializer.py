from rest_framework import serializers

from . import services


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=50)
    body = serializers.CharField(required=False, allow_blank=True, max_length=500)
    pub_date = serializers.DateTimeField()
    image = serializers.ImageField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.NewsDataClass(**data)


class TrainingProgramSerializer(serializers.Serializer):
    """

    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=2048)
    tags = serializers.CharField(max_length=255)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.TrainingProgramDataClass(**data)
