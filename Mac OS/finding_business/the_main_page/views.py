import os
from pathlib import Path
from dotenv import load_dotenv
import googlemaps
from prettytable import PrettyTable
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Load environment variables from .env
env_file = Path(__file__).resolve().parent.parent.parent.parent / '.env'
if env_file.exists():
    load_dotenv(dotenv_path=env_file)
load_dotenv()


def get_google_maps_api_key():
    key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if key and key.strip():
        return key.strip()
    for candidate in [
        Path(__file__).resolve().parent.parent / "shubham_api_key.txt",
        Path(__file__).resolve().parent.parent.parent.parent / "shubham_api_key.txt",
    ]:
        if candidate.exists():
            try:
                with open(candidate, "r") as f:
                    val = f.read().strip()
                    if val and not val.startswith("..."):
                        return val
            except Exception:
                pass
    return ""


api_key = get_google_maps_api_key()

tool_dict = {
    "viewing_map": "this is the map",
    "suitable_location": "location is suitable",
    "list_of_similar_business": "here's your list",
    "analyse_transportation": "ta ta ta ta"
}
tool_dict_display = {
    "viewing_map": "View Map of the Area",
    "list_of_similar_business": "Analyse Competition of a particular area",
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
    except Exception:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def tools(request, tool):
    try:
        tool_path = "the_main_page/tools/" + tool + ".html"
        return render(request, tool_path, {"api_key": get_google_maps_api_key()})
    except Exception:
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
    current_key = get_google_maps_api_key()
    if not current_key:
        return HttpResponse("Google Maps API key not found. Please set GOOGLE_MAPS_API_KEY in your .env file.", status=500)
    gmaps = googlemaps.Client(current_key)
    location = request.GET.get('location')
    try:
        geocode_result = gmaps.geocode(location)
        if not geocode_result:
            return HttpResponse(f"No results found for the entered location: {location}")
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        type1 = request.GET.get('type', '')
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
            'liquor shop': 'liquor_store',
            'liquor store': 'liquor_store',
        }

        place_type = type_mapping.get(type1.lower().strip() if type1 else '', type1)

        places_result = gmaps.places_nearby(
            location=(lat, lng), radius=500, type=place_type)
        for place in places_result.get('results', []):
            x.add_row([place.get('name', 'N/A'), place.get('vicinity', 'N/A')])

        table_html = x.get_html_string()
        return render(request, "the_main_page/tools/result/list_sim_bus_result.html", {'table_html': table_html})
    except Exception as e:
        return HttpResponse(f"Error fetching Google Maps data: {e}", status=500)


def footfall_analysis(request):
    current_key = get_google_maps_api_key()
    if not current_key:
        return HttpResponse("Google Maps API key not found. Please set GOOGLE_MAPS_API_KEY in your .env file.", status=500)
    gmaps = googlemaps.Client(current_key)
    location = request.GET.get('location')
    try:
        geocode_result = gmaps.geocode(location)
        if not geocode_result:
            return HttpResponse(f"No results found for the entered location: {location}")
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        business_type = request.GET.get('type')
        radius = 1000
        places_result = gmaps.places_nearby(
            location=(lat, lng), radius=radius, type=business_type)
        total_reviews = 0
        num_businesses = 0
        output_data = []
        for place in places_result.get('results', []):
            place_details = gmaps.place(place['place_id'], fields=[
                                        'name', 'rating', 'user_ratings_total'])
            if 'rating' in place_details.get('result', {}) and 'user_ratings_total' in place_details.get('result', {}):
                total_reviews += place_details['result']['user_ratings_total']
                num_businesses += 1
                output_data.append({
                    'name': place_details['result']['name'],
                    'rating': place_details['result']['rating'],
                    'total_reviews': place_details['result']['user_ratings_total']
                })
        return render(request, "the_main_page/tools/result/footfall_analysis.html", {'output_data': output_data})
    except Exception as e:
        return HttpResponse(f"Error fetching Google Maps data: {e}", status=500)


def get_transport_distances(current_key, origin, destination_type):
    gmaps = googlemaps.Client(current_key)

    transport_stations = gmaps.places_nearby(
        location=origin,
        radius=500,
        type=destination_type
    )

    if not transport_stations.get('results'):
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
    current_key = get_google_maps_api_key()
    if not current_key:
        return HttpResponse("Google Maps API key not found. Please set GOOGLE_MAPS_API_KEY in your .env file.", status=500)
    location = request.GET.get('location')
    gmaps = googlemaps.Client(current_key)
    try:
        geocode_result = gmaps.geocode(location)

        if not geocode_result:
            return HttpResponse(f"No results found for the entered location: {location}")

        origin = (geocode_result[0]['geometry']['location']['lat'],
                  geocode_result[0]['geometry']['location']['lng'])

        metro_distance = get_transport_distances(current_key, origin, "subway_station")
        bus_station_distance = get_transport_distances(
            current_key, origin, "bus_station")
        nearest_public_transport_distance = get_transport_distances(
            current_key, origin, "transit_station")

        x = PrettyTable()
        x.field_names = ["Transport Type", "Distance"]
        x.add_row(["Metro", metro_distance.get("subway_station", "N/A")])
        x.add_row(["Bus Station", bus_station_distance.get("bus_station", "N/A")])
        x.add_row(["Nearest Public Transport",
                  nearest_public_transport_distance.get("transit_station", "N/A")])
        table_html = x.get_html_string()
        return render(request, "the_main_page/tools/result/res_analyse_transport.html", {'table_html': table_html})
    except Exception as e:
        return HttpResponse(f"Error calculating transport distances: {e}", status=500)

