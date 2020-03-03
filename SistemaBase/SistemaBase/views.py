from django.http import HttpResponse
import datetime
# from django.template import Context
# from django.template import loader
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    nuevaPersona = Persona("V", "T")
    nombre = "Victor Hugo"
    apellido = "Tello"
    fechaActual = datetime.datetime.now()
    # forma de cargar directo la plantilla
    ''''documentoExterno = open(
        "C:/Users/Hugo/Documents/Django/SistemaBase/"
        "SistemaBase/plantillas/miplantilla.html"
    )'''
    # plt = Template(documentoExterno.read())
    # documentoExterno.close()
    ''''documentoExterno = loader.get_template('miplantilla.html')
    contexto = Context(
        {"nombrePersona": nombre, "apellidoPersona": apellido,
            "fechaActual": fechaActual, "persona": nuevaPersona,
            "temas":
                ["Plantillas", "Modelos",
                    "Formularios", "Vistas", "Despliegue"]}
    )'''
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    # se puede pasar de manera directa sin necesidad del contexto
    # documento = documentoExterno.render(contexto)
    # return HttpResponse(documento)
    return render(request, 'miplantilla.html', {
        "nombrePersona": nombre, "apellidoPersona": apellido,
        "fechaActual": fechaActual, "persona": nuevaPersona,
        "temas": temas})


def despedida(request):
    return HttpResponse("Adios")


def fecha(request):
    fechaActual = datetime.datetime.now()
    documento = "<html><body><h3>%s</h3></body></html>" % fechaActual
    return HttpResponse(documento)


def calcularEdad(request, anio, edad):
    periodo = anio - 2020
    edadFutura = edad + periodo
    documento = """<html>
        <body><h3>en el año %s tendras %s años</h3></body>
        </html>""" % (anio, edadFutura)
    return HttpResponse(documento)
