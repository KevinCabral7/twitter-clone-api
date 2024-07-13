from django import forms
from django.db import models
from Api import settings
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=30)
#     date_joined = models.DateTimeField(auto_now_add=True)

class Post(models.Model): 
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    # content_image = models.ImageField()
    # like = models.IntegerField()
    # repost = models.IntegerField()
    # comments = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self): 
    #     return self.content