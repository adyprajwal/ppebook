from django.db import models

# Create your models here.

class numbers(models.Model):
	num_id = models.IntegerField()
	num_word = models.CharField(max_length = 15)
	num_pic = models.ImageField()
	# num_audio = models.

	def __str__(self):
		return str(self.num_id) + ' ' + self.num_word

