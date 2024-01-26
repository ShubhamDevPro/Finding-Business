from django.urls import path
from . import views
urlpatterns = [
    path("finding_business/", views.main_page),
    # path("option_1/", views.option_1),
    path("<str:tool>/", views.tools),
    path("<int:tool>/", views.tools_by_numbers),
]
