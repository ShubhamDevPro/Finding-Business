from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


def transport(request):
    try:
        return render(request, "analyse transport",
                      )
    except:
        return HttpResponseNotFound("page not found")
