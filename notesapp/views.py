from django.shortcuts import render,redirect  
#from django.contrib.auth.forms import UserCreationFormib
from django.contrib.auth.models import User
from .models import Regist
from .forms import NewRegist
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . textIA import obtener_links_recomendacion

def home(request):
    return render(request, 'app/home.html')


def comida(request):
    if request.method == 'GET':
        return render(request, 'app/comida.html')
    else:
        print(request.POST)
        form= NewRegist(request.POST)
        if request.POST['password'] == request.POST['password2']:
            #form = NewRegist(request.POST).
           print(form)
           if form.is_valid():
            form.save()
            print(request.POST.get('nombre'))
           else:
               return HttpResponse('El')
        else:
            return HttpResponse('La contraseña esta mal')
    return redirect('/')     
   
   

def principal(request):
    
    return render(request, 'app/principal.html')

def prueva(request):
    if request.method == "GET":
        print('Todo bien con el archivo prueba')
    else:
        print(request.POST)
    return render(request, 'app/prueva.html')

def ajustes(request):
    return render(request, 'app/ajustes.html')

def post(request):
    print(request.POST)
    return redirect('home')

@csrf_exempt  # Solo para fines de ejemplo. Deberías usar CSRF de manera adecuada en producción.
def analizar_texto_view(request):
    if request.method == 'GET':
        print('estamos dentro de la funcion analizar texto desde Views')
        actividad = request.GET.get('actividad', '')
        links_recomendados = obtener_links_recomendacion(actividad)
        for link in links_recomendados:
            print(link)
        return JsonResponse(links_recomendados, safe=False)
    return JsonResponse([], safe=False)