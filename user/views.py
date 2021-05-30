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
import random
import os
from twilio.rest import Client
# Create your views here.

@api_view(['POST'])
def phoneOTP(request):
    if request.method == 'POST':
        gen_otp = random.randint(1000,9999)
        #phone = request.POST.get('phone')
        # account_sid = os.environ['AC614ea6e599d1f201e132b1e7b9e45fa2']
        # auth_token = os.environ['cbbcd8d1f8b4f472f2b46c8ff4ad2392']
        phone = request.data['phone']
        account_sid = 'AC614ea6e599d1f201e132b1e7b9e45fa2'
        auth_token = 'cbbcd8d1f8b4f472f2b46c8ff4ad2392'
        client = Client(account_sid, auth_token)
        #print('+88'+str(phone))

        message = client.messages.create(
                body='Your OTP is  '+str(gen_otp)+' this will be destroyed after 3 min. Thank you for registering into Municipal Corporation Complain Management System',
                from_='+17742373088',
                # to=str(phone)
                # to = '+8801771042196'
                to = '+88'+str(phone)
            )
        return Response({'otp': gen_otp,'message' : 'otp send to '+str(phone)})



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