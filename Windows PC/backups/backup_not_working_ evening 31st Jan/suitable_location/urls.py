from django.urls import path
from . import views
urlpatterns = [
    path("suitable_location/", views.index, name="map"),
]
