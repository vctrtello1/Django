from django.http import HttpResponse
import datetime


def saludo(request):
    documento = "<html><body><h3>Hola</h3></body></html>"
    return HttpResponse(documento)


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
