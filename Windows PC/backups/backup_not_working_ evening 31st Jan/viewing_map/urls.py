from django.urls import path
from . import views
urlpatterns = [
    path("viewing_map/", views.index, name="map"),
]
