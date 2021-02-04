from django.shortcuts import render
from .models import Notice
from .serializers import NoticeSerializer
from rest_framework import viewsets
from .pagination import LimitofPage
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,SAFE_METHODS
# Create your views here.

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer
    pagination_class = LimitofPage
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAdminUserOrReadOnly,)
