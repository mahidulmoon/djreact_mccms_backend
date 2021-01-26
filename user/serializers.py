from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username', 'password','email','first_name','last_name','is_staff','is_superuser']
        extra_kwargs = {'password': {'write_only':True, 'required':True}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = "__all__"