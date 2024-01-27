from django.urls import path
from . import views
urlpatterns = [
    # will trigger the view.py file outside the "the_main_page" folder
    path("", views.index),
    # path("finding_business/", views.main_page),
    # path("option_1/", views.option_1),
    path("<int:tool>/", views.tools_by_numbers),
    path("<str:tool>/", views.tools, name="tools"),
]
