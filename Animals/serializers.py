from rest_framework import serializers
from . models import animal

class animalSerializer(serializers.ModelSerializer):

	class Meta:
		model = animal
		fields = '__all__'