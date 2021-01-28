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
	image_field=models.ImageField(upload_to='files/',default='files/logo512.png')
	created_at=models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.complain_subject

	def avg_rating(self):
		sum = 0
		ratings = Ratings.objects.filter(complain_id=self)
		for rating in ratings:
			sum+=rating.rating
		if len(ratings)>0:
			return sum/len(ratings)
		else:
			return 0




class Ratings(models.Model):
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	complain_id = models.ForeignKey(Complain_table,on_delete=models.CASCADE)
	rating = models.DecimalField(max_digits=2,decimal_places=1,validators=[
        MinValueValidator(1),MaxValueValidator(5)
    ])