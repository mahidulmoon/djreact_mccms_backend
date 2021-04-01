from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Complain_table,Ratings
from .serializers import ComplainSerializer,ComplaineRatingSerializer
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

    def list(self,request):
        queryset = Complain_table.objects.filter(complainer_email=request.user.email)
        serializer = ComplainSerializer(queryset,many=True)
        return Response(serializer.data)


class ComplainRatingViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = ComplaineRatingSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)
