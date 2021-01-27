from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer,UserSerializer
from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import ListPagination
from rest_framework.filters import SearchFilter
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = ListPagination
    filter_backends = [SearchFilter]
    search_fields = ('id','phone')

class PreviligedUser(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    pagination_class = ListPagination
    filter_backends = [SearchFilter]
    search_fields = ('id','email','username')
