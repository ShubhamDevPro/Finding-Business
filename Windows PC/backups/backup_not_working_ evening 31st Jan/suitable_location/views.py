from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    try:
        return render(request, "suitable location",
                      )
    except:
        return HttpResponseNotFound("page not found")
