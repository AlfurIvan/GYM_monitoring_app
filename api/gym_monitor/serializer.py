from rest_framework import serializers

from user import serializer as user_serializer
from . import services
from . import models


class NewsCommentSerializer(serializers.ModelSerializer):
    author = user_serializer.UserSerializer(read_only=True)

    class Meta:
        model = models.NewsComment
        fields = ["id", "body", "pub_date", "author"]


class NewsSerializer(serializers.ModelSerializer):
    comments = NewsCommentSerializer(many=True)

    class Meta:
        model = models.News
        fields = ["id", "title", "body", "pub_date", "image", "comments"]


class TrainingProgramSerializer(serializers.Serializer):
    """

    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=2048)
    tags = serializers.CharField(max_length=255)
    image = serializers.ImageField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.TrainingProgramDataClass(**data)
