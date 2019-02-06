from rest_framework import serializers
from . models import barna

class barnaSerializer(serializers.ModelSerializer):

	class Meta:
		model = barna
		fields = '__all__'