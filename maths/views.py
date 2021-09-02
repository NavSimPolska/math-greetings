from django.shortcuts import render
from django.http import HttpResponse

def math(request):
   return HttpResponse("Tu będzie matma")

def add(request, a, b):
   return HttpResponse(a + b)

def sub(request, a, b):
   return HttpResponse(a - b)

def mul(request, a, b):
   return HttpResponse(a * b)

def div(request, a, b):
   if b == 0:
           return HttpResponse("Pamietaj cholero nigdy nie dziel przez zero!")
   return HttpResponse(a / b)