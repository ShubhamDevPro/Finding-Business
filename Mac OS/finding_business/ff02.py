import json

print("Welcome to Finding-Business.io")
print("With our software you can find the perfect location to start your new business.")
my_dict = {}
from prettytable import PrettyTable
from gmplot import gmplot
x = PrettyTable()
x.field_names = ["Business", "Address"]

def choices():
    print("What do you want to do today? ")
    print("1. Get list of similar business in area")
    print("2. View Location on Map")
    print("3. Find if the location is suitable (on the basis of footfall) ")
    print("4. Analyse Public Transportation in Area")
    choice = int(input("Enter Choice No.: "))
    if choice == 1:
        api_file = open("shubham_api_key.txt", "r")
        api_key = api_file.read()
        api_file.close()
        import googlemaps
        gmaps = googlemaps.Client(api_key)
        location = input("Enter a location: ")
        geocode_result = gmaps.geocode(location)
        if not geocode_result:
            print("No results found for the entered location.")
            choices()
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        type1 = input("Enter type of Business: ")

        type_mapping = {
            'jeweler': 'jewelry_store',
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

        places_result = gmaps.places_nearby(location=(lat, lng), radius=500, type=place_type)
        locations = []
        for place in places_result['results']:
            lat_lng = f"{place['geometry']['location']['lat']}, {place['geometry']['location']['lng']}"
            x.add_row([place['name'], lat_lng])
            locations.append({'name': place['name'], 'lat_lng': lat_lng})


choices()
