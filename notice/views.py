from django.shortcuts import render
from .models import Notice
from .serializers import NoticeSerializer
from rest_framework import viewsets
# Create your views here.


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer