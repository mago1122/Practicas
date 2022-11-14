from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import *

# Create your views here.

def inicio(request):
    return render(request, "appcoder/base.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")