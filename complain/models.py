from django.db import models

# Create your models here.
class Complain_table(models.Model):
	complainer_name=models.CharField(max_length=50)
	complainer_email=models.EmailField(max_length=255)
	complainer_phone_number=models.CharField(max_length=15)
	complaint_address=models.TextField()
	complaint_postal_code=models.CharField(max_length=20)
	complain_subject=models.CharField(max_length=100)
	complain=models.TextField()
	image_field=models.ImageField(upload_to='files/',default='files/logo512.png')
	created_at=models.DateTimeField(auto_now_add=True,blank=True)