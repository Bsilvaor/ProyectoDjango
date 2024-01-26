from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de tu app llamada Calculadora.")
@csrf_exempt
def sumar(request, op1, op2):
    return HttpResponse(op1+op2)
@csrf_exempt
def restar(request, op1, op2):
    return HttpResponse(op1-op2)
@csrf_exempt
def multi(request, op1, op2):
    return HttpResponse(op1*op2)
@csrf_exempt
def div(request, op1, op2):
    try:
        result = op1/op2
    except ZeroDivisionError:
        result = "No division by zero allowed!"
    return HttpResponse(result)


@csrf_exempt
def tu_vista(request):
    # Tu lógica de vista aquí
    return HttpResponse('OK')
