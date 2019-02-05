from rest_framework import serializers
from . models import color

class colorSerializer(serializers.ModelSerializer):

	class Meta:
		model = color
		fields = '__all__'