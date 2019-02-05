from django.db import models

# Create your models here.

class numbers(models.Model):
	num_id = models.IntegerField()
	num_word = models.CharField(max_length = 15)
	num_pic = models.ImageField()
	num_audio = models.FileField(default='')
