import json
from django.shortcuts import render
from rest_framework import viewsets, generics
from twitter.models import Post
from twitter.serializers import UserSerializer, PostSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PostCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(profile=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid(): 
            serializer.save(profile=self.request.user)
        else:
            print(serializer.errors)


class PostDelete(generics.DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(profile=user)





# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = UserSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# def login_view(request):
#     print(request)
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(data['username'], data['password'])
#         user = authenticate(username=data['username'], password=data['password'])
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'boa': 'boa'})
#         else:
#             # Return an 'invalid login' error message
#             return JsonResponse({'error': 'Invalid login credentials'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})