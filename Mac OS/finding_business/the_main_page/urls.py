from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="the_main_page"),
    # path("finding_business/", views.main_page),
    # path("option_1/", views.option_1),
    path('result/', views.show_result_list_of_sim_bus,
         name='show_result_list_of_sim_bus'),
    path('result_analysis/', views.footfall_analysis,
         name='footfall_analysis'),
    path('result_transport/', views.display_transport_distances,
         name='display_transport_distances'),
    path("<int:tool>/", views.tools_by_numbers),
    path("<str:tool>/", views.tools, name="tools"),
]
