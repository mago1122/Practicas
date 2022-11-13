from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def vista_saludo(request):
    return HttpResponse("<h1>Hola Coders! :D</h1>")

def dia_hoy(request, nombre):
    hoy = datetime.now()
    respuesta = (f"Hoy es: {hoy} y tu nombre es: {nombre}")
    return HttpResponse(respuesta)

def anio_nacimiento(request, edad):
    edad = int(edad)
    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en el año: {anio_nac}")

def vista_plantilla(request):

    archivo = open(r"C:\Users\Pleya\Desktop\CH - Python\desafio\practica\practica\templates\plantilla_1.html") 

    plantilla = Template(archivo.read()) #Se carga en memoria nuestro documento, plantilla_1.
    #notese que archivo.read esta haciendo la asociacion.

    archivo.close() #cerramos el archivo
    
    contexto = Context()

    documento = plantilla.render(contexto) #renderizamos la plantilla que ira en documento

    return HttpResponse(documento)

def vista_listado_alumnos(request):

    #abrimos el archivo
    archivo = open(r"C:\Users\Pleya\Desktop\CH - Python\desafio\practica\practica\templates\listado_alumnos.html")

    #creamos el template
    plantilla = Template(archivo.read())

    #cerramos el archivo para liberar recursos
    archivo.close()

    #Creamos el diccionario de contexto/datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Martin Lopes", "Cristian Garcia", "Nicolas Coca", "La tota Porota", "Tu vieja en tanga"]

    datos = {"tecnologia": "Caca", "listado_alumnos": listado_alumnos}

    #creamos el contexto
    contexto = Context(datos)

    #renderizamos
    documento = plantilla.render(contexto)

    return HttpResponse(documento)
