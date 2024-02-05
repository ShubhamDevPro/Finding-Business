from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_list_of_similar),
    path('list_of_similar_businesses', views.list_of_similar_business)
]
