from django.shortcuts import render
from rest_framework import viewsets
from twitter.models import Profile, Post
from twitter.serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    