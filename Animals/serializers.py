from rest_framework import serializers
from . models import Animal

class animalSerializer(serializers.ModelSerializer):

	class Meta:
		model = Animal
		fields = '__all__'