from rest_framework import serializers
from .models import CoverNewz

class CoverNewzSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverNewz
        fields = "__all__"