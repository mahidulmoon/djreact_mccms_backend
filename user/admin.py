from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileShow(admin.ModelAdmin):
    list_display = ("user","phone","address")

admin.site.register(UserProfile,UserProfileShow)