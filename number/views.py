from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import numbers
from . serializers import numberSerializer

# Create your views here.

class numberList(APIView):

	def get(self, request):
		num1 = numbers.objects.all()
		#num1 = numbers.objects.filter(num_id=1)
		serializer = numberSerializer(num1, many = True)
		return Response(serializer.data)

	def post(self):
		pass

