from rest_framework import serializers
from .models import Complain_table


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_table
        fields = ('id','complainer_name','complainer_email','complainer_phone_number','complaint_address','complaint_postal_code','complain_subject','complain','image_field','created_at','avg_rating')