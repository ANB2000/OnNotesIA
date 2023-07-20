from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')
def comida(request):
    return render(request, 'app/comida.html')
def principal(request):
    return render(request, 'app/principal.html')