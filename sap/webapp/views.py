from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from personas.models import Persona


def bienvenido(request):
    noPersonas = Persona.objects.count()
    #personas = Persona.objects.all() #Recupero all objects from bd
    personas = Persona.objects.order_by('id') #Recupero datos y los ordeno
    return render(request, 'index.html', {'noPersonas': noPersonas, 'personas': personas})


