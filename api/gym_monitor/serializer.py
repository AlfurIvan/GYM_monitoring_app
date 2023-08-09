from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=50)
    body = serializers.CharField(required=False, allow_blank=True, max_length=500)
    pub_date = serializers.DateTimeField()
    # image = serializers.ImageField

    def create(self, validated_data):
        """
        Create and return a new 'News' instance given the validated data.
        """
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('title', instance.body)
        instance.pub_date = validated_data.get('title', instance.pub_date)
        # instance.image = validated_data.get('title', instance.image)

    class Meta:
        model = News
        fields = ['title','body','pub_date']  # ,'image'