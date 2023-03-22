from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
#from rest_framework import generics, permissions

#from rest_framework import generics # List view and Detail view
from rest_framework import viewsets # viewsets replace both List view and Detail view

from rest_framework.permissions import IsAdminUser

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet): #replaces both Post List/Detail views
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): # replaces both User List/Detail views
  permission_classes = [IsAdminUser]  # only admin can view/edit/update/del users
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
