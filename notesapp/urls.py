from django.urls import path
from . views import home, comida, principal,prueva,ajustes,post,analizar_texto_view


urlpatterns = [
    path('', home, name='index'),
    path('registro/', comida, name='comida'),
    path('principal/', principal, name='principal'),
    path('prueva/', prueva, name='prueva'),
    path('ajustes/', ajustes, name='ajustes'),
    path('post/', post, name='Post'),
    path('obtener_links_recomendacion/', analizar_texto_view, name='obtener_links_recomendacion'),
]

