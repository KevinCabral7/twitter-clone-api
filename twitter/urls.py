from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostCreate.as_view(), name='post-list'),
    path('post/delete/<int:pk>',views.PostDelete.as_view(), name='delete-post')
]