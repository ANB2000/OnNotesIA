from django.urls import path
from . views import home, comida

urlpatterns = [
    path('', home, name='index'),
    path('registro/', comida, name='comida'),
]
