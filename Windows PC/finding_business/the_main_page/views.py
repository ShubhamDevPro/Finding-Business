from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse -> Object 

# Create your views here.

def index(request): # a parameter "request" is passed and the function returns a response
    return HttpResponse("this is the main page") 