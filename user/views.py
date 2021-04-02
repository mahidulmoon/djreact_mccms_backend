from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer,UserSerializer
from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from .pagination import ListPagination
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from complain.models import Complain_table
from notice.models import Notice
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET'])
def adminDashShort(requst):

    all_complains = Complain_table.objects.all().count()
    pending_complains = Complain_table.objects.filter(status="pending request").count()
    approve_complains = Complain_table.objects.filter(status="approved").count()
    solved_complains = Complain_table.objects.filter(status="solved").count()
    notices = Notice.objects.all().count()
    normal_user = User.objects.all().count()
    prev_user = User.objects.filter(is_staff=True).count()
    admin_user = User.objects.filter(is_superuser=True).count()
    if requst.method == 'GET':
        return Response({
            "complains":all_complains,
            "pendin_complains" : pending_complains,
            "approve_complains" : approve_complains,
            "solved_complains" : solved_complains,
            "notices" : notices,
            "normal_user" : normal_user,
            "prev_user" : prev_user,
            "admin_user" : admin_user
        })

        



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


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})