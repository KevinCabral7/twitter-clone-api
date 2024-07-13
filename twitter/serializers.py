from twitter.models import Post
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    profile_username = serializers.SerializerMethodField()
    class Meta: 
        model = Post
        fields = ['id', 'content', 'created_at', 'profile', 'profile_username']
        extra_kwargs = {"profile": {"read_only": True}}

    def get_profile_username(self, obj):
        return obj.profile.username