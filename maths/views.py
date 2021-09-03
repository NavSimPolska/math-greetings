from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def math(request):
   return HttpResponse("Tu będzie matma")

def add(request, a, b):
   a,b = int(a), int(b)
   wynik = a + b
   t = loader.get_template("maths/main.html")
   c = {"a": a, "b": b, "operacja": "+", "wynik" : wynik}
   return HttpResponse(t.render(c))

def sub(request, a, b):
   a,b = int(a), int(b)
   wynik = a - b
   t = loader.get_template("maths/main.html")
   c = {"a": a, "b": b, "operacja": "-", "wynik" : wynik}
   return HttpResponse(t.render(c))

def mul(request, a, b):
   a,b = int(a), int(b)
   wynik = a * b
   t = loader.get_template("maths/main.html")
   c = {"a": a, "b": b, "operacja": "*", "wynik" : wynik}
   return HttpResponse(t.render(c))

def div(request, a, b):
   a, b = int(a), int(b)
   if b == 0:
      wynik = " Pamietaj cholero nigdy nie dziel przez zero!"
   else:
      wynik = str(a / b)
   t = loader.get_template("maths/main.html")
   c = {"a": a, "b": b, "operacja": "/", "wynik" : wynik.upper()}
   return HttpResponse(t.render(c))