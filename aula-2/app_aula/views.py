from django.shortcuts import render
from django.http import HttpResponse

def func1(request):
    return render(request, "app_aula/index.html")
# Create your views here.

def sobre(request):
    return render(request, "app_aula/sobre.html")

def inicio(request):
    return render(request, "app_aula/inicio.html")