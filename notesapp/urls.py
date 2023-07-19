from django.urls import path
from . views import home, comida, principal,prueva

urlpatterns = [
    path('', home, name='index'),
    path('registro/', comida, name='comida'),
    path('principal/', principal, name='principal'),
    path('prueva/', prueva, name='prueva'),
]
