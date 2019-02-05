from django.db import models

# Create your models here.

class animal(models.Model):
	animal_id = models.IntegerField()
	animal_word = models.CharField(max_length = 15)
	animal_pic = models.ImageField()
	animal_audio = models.FileField(default='')
