from django.db import models

# Create your models here.

class barna(models.Model):
	barna_id = models.IntegerField()
	barna_letter = models.CharField(max_length = 1, default = '')
	barna_word = models.CharField(max_length = 15)
	barna_pic = models.ImageField()
	barna_audio = models.FileField(default='')
