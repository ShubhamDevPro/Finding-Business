from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "the_main_page"),
    # path("finding_business/", views.main_page),
    # path("option_1/", views.option_1),
    path("<int:tool>/", views.tools_by_numbers),
    path("<str:tool>/", views.tools, name="tools"),
]
