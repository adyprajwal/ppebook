from django.db import models

# Create your models here.

class users(models.Model): 
	user_id = models.IntegerField()
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 15)

	def __str__(self):
		return str(self.user_id) + ' ' + self.first_name + ' ' + self.last_name
