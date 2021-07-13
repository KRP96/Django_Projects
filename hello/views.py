from django.http import HttpResponse           #import HttpResponse 
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")        #use HttpResponse keyword