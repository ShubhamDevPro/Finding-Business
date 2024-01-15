print("Welcome to Finding-Business.io")
print("With our software you can find the perfect location to start your new business.")
my_dict = {}
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Business","Address"]

def choices():
    print("What do you want to do today? ")
    print("1. Get list of similar business in area")
    print("2. View Location on Map")
    print("3. Find if the location is suitable (on the basis of footfall) ")
    print("4. Analyse Public Transportation in Area")
    choice = int(input("Enter Choice No.-"))
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

        places_result = gmaps.places_nearby(location=(lat, lng), radius=500, type=type1)
        for place in places_result['results']:

            x.add_row([place['name'],place['vicinity']])
        print(x)

    elif choice == 2:
        from pprint import pprint
        import googlemaps

        api_file = open("shubham_api_key.txt", "r")
        api_key = api_file.read()
        api_file.close()
        gmaps = googlemaps.Client(api_key)
        location = input("Enter Location - ")
        geocode_result = gmaps.geocode(location)[0]['geometry']['location']
        lat = geocode_result['lat']
        lng = geocode_result['lng']

        center = (lat, lng)
        zoom = 12

        url = "https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom={}&size=800x800&key={}".format(
            center[0], center[1], zoom, api_key)

        pprint(url)

        import webbrowser

        webbrowser.open(url)
    elif choice == 3:
        import googlemaps
        import time

        api_file = open("shubham_api_key.txt", "r")
        api_key = api_file.read()
        api_file.close()
        gmaps = googlemaps.Client(api_key)
        location = input("Enter a location (e.g. address, city, or coordinates): ")
        geocode_result = gmaps.geocode(location)
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        business_type = input("Enter the type of business you're interested in (e.g. restaurant, grocery store): ")
        radius = 1000
        places_result = gmaps.places_nearby(location=(lat, lng), radius=radius, type=business_type)
        total_reviews = 0
        num_businesses = 0

        for place in places_result['results']:
            place_details = gmaps.place(place['place_id'], fields=['name', 'rating', 'user_ratings_total'])
            if 'rating' in place_details['result'] and 'user_ratings_total' in place_details['result']:
                total_reviews += place_details['result']['user_ratings_total']
                num_businesses += 1
                print(
                    f"{place_details['result']['name']}: {place_details['result']['rating']} ({place_details['result']['user_ratings_total']} reviews)")

        if num_businesses > 0:
            avg_reviews = total_reviews / num_businesses
        else:
            avg_reviews = 0
        if avg_reviews > 50:
            print(f"This location is suitable for opening a {business_type} store.")
        else:
            print(f"This location is not suitable for opening a {business_type} store.")
    elif choice == 4:
        import googlemaps

        api_file = open("shubham_api_key.txt", "r")
        api_key = api_file.read().strip()
        api_file.close()

        gmaps = googlemaps.Client(api_key)
        location = input("Enter a location (e.g. address, city, or coordinates): ")
        geocode_result = gmaps.geocode(location)
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        radius = 1000
        transit_stations_result = gmaps.places_nearby(location=(lat, lng), radius=radius, type='transit_station')
        # To find total number of ways to reach  business location-->>>
        num_transit_stations = len(transit_stations_result['results'])
        good_transportation_criteria = 5  # at least 5 transit stations within 1km radius
        if num_transit_stations >= good_transportation_criteria:
            print("Public transportation is good at this location. There are", num_transit_stations,
                  "ways to reach there in", radius, "meter radius.")
        else:
            print("Public transportation is not good at this location. There are only", num_transit_stations,
                  "ways to reach there in", radius, "meter radius.")

choices()
"""#print(place['name'])
                my_dict[place['name']] = place['vicinity']
                #print(place['vicinity'])
              """
"""
            for type1 in my_dict:
                #print(type1,my_dict.values[type1])
                print(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], sep='   |||   ')
                print("Patient_ID_number", "name_of_patient", sep=' || ') """