from django.urls import path
from . import views
urlpatterns = [
    path("analyse_transportation/", views.transport, name="transport"),
]
