from django.shortcuts import render
from rest_framework import permissions, generics, serializers, viewsets
from rest_framework.response import Response
from .models import Thread, Post, Reply
from .serializers import ThreadSerializer, PostSerializer, ReplySerializer


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: 
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True
        elif view.action in ['destroy', 'partial_update', 'updated']:
            return obj.creator == request.user
        return True

class TheadsViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [UserPermission]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [UserPermission]

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permissions_classes = [UserPermission]

        

