from django.shortcuts import render
from rest_framework import viewsets
from .models import Complain_table
from .serializers import ComplainSerializer
from .pagination import NumberOfComplain
# Create your views here.


class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain_table.objects.all().order_by('-created_at')
    serializer_class = ComplainSerializer
    pagination_class = NumberOfComplain