from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Complain_table(models.Model):
	complainer_name=models.CharField(max_length=50)
	complainer_email=models.EmailField(max_length=255)
	complainer_phone_number=models.CharField(max_length=15)
	complaint_address=models.TextField()
	complaint_postal_code=models.CharField(max_length=20)
	complain_subject=models.CharField(max_length=100)
	complain=models.TextField()
	status = models.CharField(max_length=50,default="pending request")
	image_field=models.FileField(upload_to='files/',default='files/logo512.png')
	created_at=models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.complain_subject

	def avg_rating(self):
		sum = 0
		ratings = Ratings.objects.filter(complain_id=self).count()
		return ratings




class Ratings(models.Model):
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	complain_id = models.ForeignKey(Complain_table,on_delete=models.CASCADE)
	rating = models.IntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(1)
    ])