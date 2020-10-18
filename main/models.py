from django.db import models

# Create your models here.
class Faculty_db(models.Model):
	Name = models.CharField(max_length=30)
	Subject = models.CharField(max_length=30)
	Contact = models.DecimalField(max_digits=10, decimal_places=0)
	Email = models.EmailField(max_length=254)

	def __str__(self):
		return self.Name


