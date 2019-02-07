from django.db import models

# Create your models here.

class Alphabets(models.Model):
	alpha_id = models.IntegerField()
	alpha_letter_lower = models.CharField(max_length = 1, default='')
	alpha_letter_upper = models.CharField(max_length = 1, default='')
	alpha_word = models.CharField(max_length = 15)
	alpha_gif = models.ImageField()
	word_gif = models.ImageField()
	word_audio = models.FileField(default='')

