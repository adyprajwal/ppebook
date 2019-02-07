from rest_framework import serializers
from . models import Barna

class barnaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Barna
		fields = '__all__'