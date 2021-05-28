from rest_framework import serializers
from .models import Complain_table,Ratings


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_table
        fields = ('id','complainer_name','complainer_email','complainer_phone_number','complaint_address','complaint_postal_code','complain_subject','complain','image_field','status','created_at','avg_rating')



class ComplaineRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id','user_id','complain_id','rating')



class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_table
        fields = ('id','status')