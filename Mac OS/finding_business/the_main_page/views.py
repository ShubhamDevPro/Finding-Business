import googlemaps
from prettytable import PrettyTable
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
tool_dict = {
    "viewing_map": "this is the map",
    "suitable_location": "location is suitable",
    "list_of_similar_business": "here's your list",
    "analyse_transportation": "ta ta ta ta"
}
tool_dict_display = {
    "viewing_map": "View Map of the Area",
    "list_of_similar_business": "Get list of similar business",
    "suitable_location": "Find the perfect location",
    "analyse_transportation": "Analyse transportation facilities"
}
tool_list = list(tool_dict.keys())


def index(request):
    try:
        return render(request, "the_main_page/main.html", {
            "tool_list": tool_list,
            "text": "The Main Page",
            "tool_dict_display": tool_dict_display,
            "tool_dict": tool_dict}
        )
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

    """
    try:
        
    except:
        return HttpResponseNotFound("This tool is unavailable yet")
"""


def tools(request, tool):
    try:
        # tool_path = reverse("tools", args=[tool])
        tool_path = "the_main_page/tools/"+tool+".html"
        return render(request, tool_path)
        # display_text = tool_dict_display[tool]
        # return HttpResponse(display_text)
        """
        list_items = ""
        for tool1 in tool_list:
            display_text = tool_dict_display[tool1]
            tool_path = reverse("tools", args=[tool1])
            list_items += f"<li><a href =\"{tool_path}\">{display_text}</a></li><br>"
        response_data = f"<ul>{list_items}</ul>"
        return HttpResponse(response_data)
        """
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def tools_by_numbers(request, tool):
    if tool > len(tool_dict) or tool < 1:
        return HttpResponseNotFound("Tool Unavailable at the moment")
    tool_list = list(tool_dict.keys())
    redirect_tool_key = tool_list[tool-1]
    redirect_path = reverse("tools", args=[redirect_tool_key])
    return HttpResponseRedirect(redirect_path)


def show_result_list_of_sim_bus(request):
    x = PrettyTable()
    x.field_names = ["Business", "Address"]
    api_key = "AIzaSyB5M4ndSUdCKL2nib531J1rXjoX6lGYgnE"
    gmaps = googlemaps.Client(api_key)
    location = request.GET.get('location')
    type1 = request.GET.get('type')
    geocode_result = gmaps.geocode(location)
    if not geocode_result:
        error_message = "No results found for the entered location."
        return render(request, 'your_template.html', {'error_message': error_message})

    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    places_result = gmaps.places_nearby(
        location=(lat, lng), radius=500, type=type1)

    for place in places_result['results']:
        x.add_row([place['name'], place['vicinity']])

    table_html = x.get_html_string()
    return render(request, "the_main_page/tools/result/list_sim_bus_result.html", {'table_html': table_html})

    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        result = number1 + number2
        tool_path = reverse("show_result")
        # return render(request, 'list_sum_bus_result.html', {'result': result})
        return render(request, "the_main_page/tools/result/list_sim_bus_result.html", {
            "result": result}
        )
    else:
        # Handle GET requests
        return render(request, 'list_sim_bus_result.html')


def footfall_analysis(request):
    api_key = "AIzaSyB5M4ndSUdCKL2nib531J1rXjoX6lGYgnE"
    gmaps = googlemaps.Client(api_key)
    location = request.GET.get('location')
    # type1 = request.GET.get('type')
    gmaps = googlemaps.Client(api_key)
    # location = input("Enter a location (e.g. address, city, or coordinates): ")
    geocode_result = gmaps.geocode(location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    radius = 1000
    places_result = gmaps.places_nearby(
        location=(lat, lng), radius=radius, type=business_type)
    total_reviews = 0
    num_businesses = 0
