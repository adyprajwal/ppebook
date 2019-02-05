from django.db import models

# Create your models here.

class color(models.Model):
	color_id = models.IntegerField()
	color_name = models.CharField(max_length = 15)
	color_pic = models.ImageField()
	color_audio = models.FileField(default='')
