from rest_framework import serializers

from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author']


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'post']
