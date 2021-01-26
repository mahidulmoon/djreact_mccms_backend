from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import ListPagination
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = ListPagination

