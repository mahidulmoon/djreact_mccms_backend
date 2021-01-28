from rest_framework import serializers
from .models import Complain_table


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_table
        fields = "__all__"