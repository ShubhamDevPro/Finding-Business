from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage_list_of_similar_business(request):
    return HttpResponse("home page")


def list_of_similar_business(request):
    return HttpResponse("Here is the list of similar business")
