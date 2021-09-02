from django.shortcuts import render
from django.http import HttpResponse

def ogolne(request):
    return HttpResponse("Hello World!!!!")

def imie(request, a):
    a = f'Hello {a.capitalize()}!'
    return HttpResponse(a)