from django.contrib import admin
from .models import Notice
# Register your models here.

class NoticeDisplay(admin.ModelAdmin):
    list_display = ('subject','department','notice','created_at')


admin.site.register(Notice,NoticeDisplay)