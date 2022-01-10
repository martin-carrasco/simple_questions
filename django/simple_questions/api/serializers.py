from django.db.models.fields import IntegerField
from rest_framework import serializers

from .models import Post, Reply, Thread


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'creator', 'updated_at', 'created_at', 'score', 'thread', 'accepted', 'main']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'content', 'creator', 'updated_at', 'created_at', 'score', 'post']

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'title', 'creator', 'updated_at', 'created_at', 'views']
