from django.urls import path
from . views import home, comida, principal

urlpatterns = [
    path('', home, name='index'),
    path('registro/', comida, name='comida'),
    path('principal/', principal, name='principal'),
]
