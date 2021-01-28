from django.contrib import admin
from .models import Complain_table
# Register your models here.

class ComplainShow(admin.ModelAdmin):
    list_display = ('complainer_email','complainer_phone_number','complain_subject','created_at')


admin.site.register(Complain_table,ComplainShow)