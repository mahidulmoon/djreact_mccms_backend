from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Complain_table
from .serializers import ComplainSerializer
from .pagination import NumberOfComplain
from rest_framework.response import Response
# Create your views here.


class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain_table.objects.all().order_by('-created_at')
    serializer_class = ComplainSerializer
    pagination_class = NumberOfComplain
    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)