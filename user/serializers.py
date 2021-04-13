from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','is_staff','is_superuser']
        extra_kwargs = {'password': {'write_only':True, 'required':True}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = ('user','phone','address')
    
    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(),validated_data=user_data)
        Token.objects.create(user=user)
        UserProfile.objects.create(user=user,phone=validated_data.pop('phone'),address=validated_data.pop('address'))
        return user