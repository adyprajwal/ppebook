from django.urls import path, include
from number import views as numview
from rest_framework import routers
from alpha import views as alphaview
from Animals import views as animalview
from color import views as colorview

router = routers.DefaultRouter()
router.register('Numbers', numview.NumberView)
router.register('Alphabets', alphaview.AlphaView)
router.register('Animals', animalview.AnimalView)
router.register('Colors', colorview.ColorView)

urlpatterns = [
	path('', include(router.urls))
]