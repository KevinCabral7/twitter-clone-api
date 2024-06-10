from twitter.models import Profile, Post
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = '__all__'