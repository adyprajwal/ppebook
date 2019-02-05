from rest_framework import serializers
from .models import Alphabets

class AlphaSerializers(serializers.ModelSerializer):
	class Meta:
		model = Alphabets
		fields = '__all__'
