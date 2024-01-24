from django.urls import path
from . import views
urlpatterns = [
    path("finding_business/", views.index)
]
