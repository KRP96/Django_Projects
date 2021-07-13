from django.http import HttpResponse           #import HttpResponse 
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")       


def brian(request):
    return HttpResponse("Hello, Brian!")  #use HttpResponse keyword

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")