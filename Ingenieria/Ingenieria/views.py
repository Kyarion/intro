from django.http import HttpResponse
from django.template import Template, Context

def principal(request):
    plantilla = open("C:/Users/juanv/OneDrive/Escritorio/Cosas extras/Proyecto Ingenieria/Django/Ingenieria/Ingenieria/Plantillas/Plantilla1.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Puntos(request):
    plantilla = open("C:/Users/juanv/OneDrive/Escritorio/Cosas extras/Proyecto Ingenieria/Django/Ingenieria/Ingenieria/Plantillas/PlantillaPuntos.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Canjes(request):
    plantilla = open("C:/Users/juanv/OneDrive/Escritorio/Cosas extras/Proyecto Ingenieria/Django/Ingenieria/Ingenieria/Plantillas/PlantillasCanjes.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Misiones(request):
    plantilla = open("C:/Users/juanv/OneDrive/Escritorio/Cosas extras/Proyecto Ingenieria/Django/Ingenieria/Ingenieria/Plantillas/PlantillaMisiones.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Usuario(request):
    plantilla = open("C:/Users/juanv/OneDrive/Escritorio/Cosas extras/Proyecto Ingenieria/Django/Ingenieria/Ingenieria/Plantillas/PlantillasUsuarios.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)