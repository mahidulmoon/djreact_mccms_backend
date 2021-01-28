from django.db import models

# Create your models here.

class Notice(models.Model):
    subject = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    notice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)