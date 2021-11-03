from django.db import models

# Create your models here.
class MenuItem(models.Model):
	price = models.DecimalField(max_digits=7, decimal_places=2)
	name = models.CharField(max_length=120)
	catagory = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to = "images/")

	def __str__(self):
		return self.name