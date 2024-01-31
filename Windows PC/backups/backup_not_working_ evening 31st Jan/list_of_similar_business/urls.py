from django.urls import path
from . import views
urlpatterns = [
    path("list_of_similar_business/", views.index, name="map"),
]
