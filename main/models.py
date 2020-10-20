from django.db import models

# Create your models here.
class Faculty_db(models.Model):
	Name = models.CharField(max_length=30)
	Subject = models.CharField(max_length=30)
	Contact = models.DecimalField(max_digits=10, decimal_places=0)
	Email = models.EmailField(max_length=254)
	#Payment
	#Attendance

	def __str__(self):
		return self.Name

class Student_db(models.Model):
	options = [('First','1'),('Second','2'),('Third','3'),('Fourth','4'),('Fifth','5'),('Sixth','6'),
	('seventh','7'),('eigth','8'),('Ninth','9'),('Tenth','10')]

	
	Name = models.CharField(max_length=30)
	BirthDate = models.DateField(null=True, blank=True)
	Class =  models.CharField(max_length=10, choices= options, default = 'First')
	#Result
	Parents_Contact_Number = models.DecimalField(max_digits=10, decimal_places=0)
	Email = models.EmailField(max_length=254, null= True, blank= True)
	#Fee
	#Attendance

	class Meta:
		ordering = ['Class']

	def __str__(self):
		return self.Name

