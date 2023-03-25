
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=70)
    sub_title = serializers.CharField(
        max_length=250)
    slug = serializers.SlugField()
    author = serializers.StringRelatedField()
