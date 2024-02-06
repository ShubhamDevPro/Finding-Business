import googlemaps
from prettytable import PrettyTable
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
api_key = "AIzaSyB5M4ndSUdCKL2nib531J1rXjoX6lGYgnE"
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
    geocode_result = gmaps.geocode(location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    type1 = request.GET.get('type')
    type_mapping = {
        'jeweller': 'jewelry_store',
        'ca office': 'accounting',
        'barber': 'beauty_salon',
        'hair salon': 'beauty_salon',
        'stationary': 'book_store',
        'library': 'book_store',
        'coffee shop': 'cafe',
        'chemist': 'pharmacy',
        'drug store': 'pharmacy',
        'petrol pump': 'gas_station',
        'fuel store': 'gas_station',
        'cinema': 'movie_theatre',
        'film hall': 'movie_theatre',
        'gym': 'fitness_centre',
        'bar': 'night_club',
        'pub': 'night_club',
        'supermarket': 'home_goods_store',
        'grocery shop': 'home_goods_store',
        'eyewear shop': 'optical_store',
        'optician': 'optical_store',
        'dental clinic': 'dentist',
        'tooth doctor': 'dentist',
        'cloth wash': 'laundry',
        'laundry store': 'laundry',
        'clinic': 'hospital',
        'chidiya ghar': 'zoo',
        'mechanic': 'car_repair_shop',
        'auto repair shop': 'car_repair_shop',
        'cake shop': 'bakery',
        'pastry shop': 'bakery',
        'art gallery': 'museum',
        'flower shop': 'florist',
        'floral boutique': 'florist',
        'mall': 'shopping_mall',

    }

    # Use the mapping or default to user input
    place_type = type_mapping.get(type1, type1)

    places_result = gmaps.places_nearby(
        location=(lat, lng), radius=500, type=place_type)
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

    gmaps = googlemaps.Client(api_key)
    location = request.GET.get('location')
    # type1 = request.GET.get('type')
    geocode_result = gmaps.geocode(location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    business_type = request.GET.get('type')
    radius = 1000
    places_result = gmaps.places_nearby(
        location=(lat, lng), radius=radius, type=business_type)
    total_reviews = 0
    num_businesses = 0
    output_data = []
    for place in places_result['results']:
        place_details = gmaps.place(place['place_id'], fields=[
                                    'name', 'rating', 'user_ratings_total'])
        if 'rating' in place_details['result'] and 'user_ratings_total' in place_details['result']:
            total_reviews += place_details['result']['user_ratings_total']
            num_businesses += 1
            output_data.append({
                'name': place_details['result']['name'],
                'rating': place_details['result']['rating'],
                'total_reviews': place_details['result']['user_ratings_total']
            })
    print(output_data)
    return render(request, "the_main_page/tools/result/footfall_analysis.html", {'output_data': output_data})


def get_transport_distances(api_key, origin, destination_type):
    gmaps = googlemaps.Client(api_key)

    transport_stations = gmaps.places_nearby(
        location=origin,
        radius=500,
        type=destination_type
    )

    if not transport_stations['results']:
        return {destination_type: "N/A"}

    transport_station_location = transport_stations['results'][0]['geometry']['location']
    destination = (
        transport_station_location['lat'], transport_station_location['lng'])

    result = gmaps.distance_matrix(
        origins=origin,
        destinations=destination,
        mode="walking",
        units="metric"
    )

    if result['rows'][0]['elements'][0]['status'] == 'OK':
        distance = result['rows'][0]['elements'][0]['distance']['text']
        return {destination_type: distance}
    else:
        return {destination_type: "N/A"}


def display_transport_distances(request):
    location = request.GET.get('location')
    gmaps = googlemaps.Client(api_key)
    geocode_result = gmaps.geocode(location)

    if not geocode_result:
        print("No results found for the entered location.")
        return

    origin = (geocode_result[0]['geometry']['location']['lat'],
              geocode_result[0]['geometry']['location']['lng'])

    metro_distance = get_transport_distances(api_key, origin, "subway_station")
    bus_station_distance = get_transport_distances(
        api_key, origin, "bus_station")
    nearest_public_transport_distance = get_transport_distances(
        api_key, origin, "transit_station")

    x = PrettyTable()
    x.field_names = ["Transport Type", "Distance"]
    x.add_row(["Metro", metro_distance["subway_station"]])
    x.add_row(["Bus Station", bus_station_distance["bus_station"]])
    x.add_row(["Nearest Public Transport",
              nearest_public_transport_distance["transit_station"]])
    table_html = x.get_html_string()
    return render(request, "the_main_page/tools/result/res_analyse_transport.html", {'table_html': table_html})
