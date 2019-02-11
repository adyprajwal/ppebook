from django.urls import path, include
from number import views as numview
from rest_framework import routers
from alpha import views as alphaview
from animals import views as animalview
from color import views as colorview
from barnamala import views as barnaview

router = routers.DefaultRouter()
router.register('Numbers', numview.NumberView)
router.register('Alphabets', alphaview.AlphaView)
router.register('Animals', animalview.AnimalView)
router.register('Colors', colorview.ColorView)
router.register('BarnaMala', barnaview.BarnaView)

urlpatterns = [
	path('', include(router.urls)),
	path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]