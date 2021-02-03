from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Complain_table
from .serializers import ComplainSerializer
from .pagination import NumberOfComplain
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain_table.objects.all().order_by('-created_at')
    serializer_class = ComplainSerializer
    pagination_class = NumberOfComplain
    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ComplainPostViewSet(viewsets.ModelViewSet):
    queryset = Complain_table.objects.all()
    serializer_class = ComplainSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)