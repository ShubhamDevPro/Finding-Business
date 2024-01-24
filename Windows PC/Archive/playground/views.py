from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# basically a request handler

def say_hello(request):
    #return HttpResponse('Hello World')
    return render(request,'hello.html',{'name':'Shubham'})
