from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from maths.models import Math

from maths.models import Result


def math(request):
   return HttpResponse("Tu będzie matma")

def add(request, a, b):
      wynik = a + b
      c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
      result = Result.objects.get_or_create(value=wynik)[0]
      Math.objects.create(operation='add', a=a, b=b, result=result)
      return render(request,"maths/operation.html",c)

def sub(request, a, b):
   a,b = int(a), int(b)
   wynik = a - b
   c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "odejmowanie"}
   result = Result.objects.get_or_create(value=wynik)[0]
   Math.objects.create(operation='sub', a=a, b=b, result=result)
   return render(request, "maths/operation.html", c)

def mul(request, a, b):
   a,b = int(a), int(b)
   wynik = a * b
   c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "mnożenie"}
   result = Result.objects.get_or_create(value=wynik)[0]
   Math.objects.create(operation='mul', a=a, b=b, result=result)
   return render(request, "maths/operation.html", c)

def div(request, a, b):
   if int(b) == 0:
       wynik = None
       messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")
       c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
       result = Result.objects.get_or_create(value=wynik)[0]
       Math.objects.create(operation='div', a=a, b=b, result=result)
   else:
       wynik = a / int(b)
       c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
       result = Result.objects.get_or_create(value=wynik)[0]
       Math.objects.create(operation='div', a=a, b=b, result=result)
   return render(request, "maths/operation.html", c)

def maths_list(request):
   maths = Math.objects.all()
   return render(
       request=request,
       template_name="maths/list.html",
       context={"maths": maths}
   )

def math_details(request, id):
   math = Math.objects.get(id=id)
   return render(
       request=request,
       template_name="maths/details.html",
       context={"math": math}
   )

def results_list(request):
  if request.method == "POST":
      value = request.POST['value'] or None
      error = request.POST['error'] or None
      if value and error:
          messages.add_message(
              request,
              messages.ERROR,
              "Błąd! Podano jednocześnie value i error. Podaj tylko jedną z tych wartości"
          )
      elif value or error:

          Result.objects.get_or_create(
              value=float(value),
              error=error
          )
          messages.add_message(
              request,
              messages.SUCCESS,
              "Utworzono nowy Result!!"
          )

      else:
          messages.add_message(
              request,
              messages.ERROR,
              "Błąd! Nie podano wartości!!"
          )

  results = Result.objects.all()
  return render(
      request=request,
      template_name="maths/results.html",
      context={"results": results}
  )