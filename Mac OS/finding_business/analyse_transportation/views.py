from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage_analyse_transport(request):
    return HttpResponse("home page - analyse transport")


def analyse_transport(request):
    return HttpResponse("Analyse Transport")
