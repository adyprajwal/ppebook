from django.db import models

# Create your models here.

class Animal(models.Model):
	animal_id = models.IntegerField()
	animal_name = models.CharField(max_length = 15)
	animal_pic = models.ImageField()
	animal_audio = models.FileField(default='')
