from django.db import models

# Create your models here.

class CoverNewz(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()