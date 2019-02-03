from rest_framework import serializers
from . models import numbers

class numberSerializer(serializers.ModelSerializer):

	class Meta:
		model = numbers
		fields = '__all__'