import random
from translate import Translator
import tkinter
import textblob
import googletrans
import speech_recognition as s
import pytesseract as T
import text_to_speech as t
import PIL.Image
from PIL import ImageTk
import pickle
import tkinter
from tkinter import filedialog as f
from tkinter import *
from tkinter import ttk, messagebox
# import mysql.connector


def transport():
    root = Tk()
    root.title('Finding-Business.io')
    root.geometry('800x600')
    root['bg'] = '#ffbf00'
    style = ttk.Style()
    style.configure('Custom.TLabel', background='#ffbf00')
    # style= ttk.Style()
    style.configure('Custom.TLabel1', background='#87cefa')

    def Option3rd():
        import googlemaps
        # --------------------------------------------------------------------------------------------
        location = location_String.get()
        # business_type = type1_String.get()
        desired_output = str()
        # location = input("Enter a location (e.g. address, city, or coordinates): ")
        # business_type = input("Enter the type of business you're interested in (e.g. restaurant, grocery store): ")
        # ----------------------------------------------------------------------------------------

        api_file = open("shubham_api_key.txt", "r")
        api_key = api_file.read().strip()
        api_file.close()
        gmaps = googlemaps.Client(api_key)
        # location = input("Enter a location (e.g. address, city, or coordinates): ")
        geocode_result = gmaps.geocode(location)
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        radius = 500
        transit_stations_result = gmaps.places_nearby(
            location=(lat, lng), radius=radius, type='transit_station')
        # To find total number of ways to reach  business location-->>>
        num_transit_stations = len(transit_stations_result['results'])
        # print(num_transit_stations)
        good_transportation_criteria = 5
        # Criteria = at least 5 transit stations within 1km radius
        if num_transit_stations >= good_transportation_criteria:
            desired_output += f"Public transportation is good at this location. There are,{num_transit_stations},ways to reach there in {radius} metre radius."
        else:
            desired_output += f"Public transportation is not good at this location. There are,{num_transit_stations},ways to reach there in {radius} metre radius."
        output_text = tkinter.Text(root)
        output_text.pack()
        output_text.insert(tkinter.END, desired_output + 2 * '\n')

    # ------------------------------------------------------------------------------------------
    t = ttk.Label(root, text="Welcome to Finding-Business.io",
                  font=50, style='Custom.TLabel')
    t.pack()
    t = ttk.Label(root, text="With our software you can find the perfect location to start your new business.",
                  padding=(30, 10), style='Custom.TLabel')
    t.pack()
    # ----------------------------------------------------------------------------------------
    input_frame = ttk.Frame(root, padding=(
        20, 10, 20, 0), style='Custom.TLabel')
    input_frame.pack(fill="both")
    # ----------------------------------------------------------------------------------------
    name_label = ttk.Label(input_frame, text="Enter Location where you are planning to start business:",
                           style='Custom.TLabel')
    name_label.grid(row=0, column=0, pady=(0, 10), padx=(0, 10), )
    location_String = tkinter.StringVar()
    location_entry = tkinter.Entry(
        input_frame, width=50, textvariable=location_String)
    location_entry.grid(row=0, column=1)
    location_entry.focus()
    # ----------------------------------------------------------------------------------------
    """
    name_label2 = ttk.Label(input_frame, text="Type of Business you are interested in :", style='Custom.TLabel')
    name_label2.grid(row=1, column=0, pady=(0, 10), padx=(0, 10))
    type1_String = tk.StringVar()
    type1_entry = tk.Entry(input_frame, width=50, textvariable=type1_String)
    type1_entry.grid(row=1, column=1, pady=(0, 10))
    """
    # ----------------------------------------------------------------------------------------
    '''
    option1st_button = ttk.Button(root, text="1. Get list of similar business in area", command=Option1st)
    # option1st_button.pack(side="left",fill="x",expand=True)
    option1st_button.pack(side="left")
    quit_button = ttk.Button(root, text="Close the App", command=root.destroy)
    quit_button.pack()
    '''
    style = ttk.Style()
    style.configure('Custom.TFrame', background='#ffbf00')
    button_frame = ttk.Frame(root, style='Custom.TFrame')
    option1st_button = ttk.Button(button_frame, text="3.Analyse Public Transportation in Area",
                                  command=Option3rd)
    option1st_button.pack(side="left", fill="x", expand=True, padx=(0, 10))
    # ----------------------------------------------------------------------------------------

    def des():
        root.destroy()
    quit_button = ttk.Button(button_frame, text="Close the App", command=lambda: [
                             des(), User_Choice()])
    quit_button.pack(fill="x", expand=True)
    button_frame.pack(side="top", pady=(10, 0))

    root.mainloop()


def review():
    root = Tk()
    root.title('Finding-Business.io')
    root.geometry('800x600')
    root['bg'] = '#ffbf00'
    style = ttk.Style()
    style.configure('Custom.TLabel', background='#ffbf00')
    # style= ttk.Style()
    style.configure('Custom.TLabel1', background='#87cefa')

    # --------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------

    def Option2nd():
        import googlemaps
        import time
        api_file = open("shubham_api_key.txt", "r")
        api_key = api_file.read()
        api_file.close()
        gmaps = googlemaps.Client(api_key)
        # ----------------------------------------------------------------------------------------
        location = location_String.get()
        business_type = type1_String.get()
        desired_output = str()
        # location = input("Enter a location (e.g. address, city, or coordinates): ")
        # business_type = input("Enter the type of business you're interested in (e.g. restaurant, grocery store): ")
        # ----------------------------------------------------------------------------------------
        geocode_result = gmaps.geocode(location)
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        radius = 1000
        places_result = gmaps.places_nearby(
            location=(lat, lng), radius=radius, type=business_type)
        total_reviews = 0
        num_businesses = 0
        output_text = tkinter.Text(root)
        output_text.pack()
        for place in places_result['results']:
            place_details = gmaps.place(place['place_id'], fields=[
                                        'name', 'rating', 'user_ratings_total'])
            if 'rating' in place_details['result'] and 'user_ratings_total' in place_details['result']:
                total_reviews += place_details['result']['user_ratings_total']
                num_businesses += 1
            # desired_output+=f"{place_details['result']['name']}: {place_details['result']['rating']} ({place_details['result']['user_ratings_total']} reviews"
            # desired_output+='\n'
            # output_text.insert(tk.END,desired_output+'\n')
        if num_businesses > 0:
            avg_reviews = total_reviews / num_businesses
        else:
            avg_reviews = 0
        if avg_reviews > 50:
            '''
            desired_output+=f"Since the average number of reviews of business in the area(in a 1000 sq. m. radius)is greater than 50 i.e.{avg_reviews}.'\n" \
                            f"This location is suitable for opening a {business_type} store.'\n " \
                            f"Disclaimer:- This may not be the best criteria for anaylysis and we are working on improving the same"
            '''
            desired_output += f"Based on our algorithm,the footfall of {location} seems good'\n" \
                              f"This location is suitable for opening a {business_type} store.'\n" \
                              f"with respect to our custom criteria."

            output_text.insert(tkinter.END, desired_output + 2 * '\n')

        else:
            desired_output += f"Since the average number of reviews of business in the area(in a 1000 sq. m. radius)is less than 50 i.e.{avg_reviews}.'\n" \
                f"This location is not suitable for opening a {business_type} store.'\n " \
                f"Disclaimer:- This may not be the best criteria for anaylysis and we are working on improving the same"
            output_text.insert(tkinter.END, desired_output+2*'\n')

    # ------------------------------------------------------------------------------------------
    t = ttk.Label(root, text="Welcome to Finding-Business.io",
                  font=50, style='Custom.TLabel')
    t.pack()
    t = ttk.Label(root, text="With our software you can find the perfect location to start your new business.",
                  padding=(30, 10), style='Custom.TLabel')
    t.pack()
    # ----------------------------------------------------------------------------------------
    input_frame = ttk.Frame(root, padding=(
        20, 10, 20, 0), style='Custom.TLabel')
    input_frame.pack(fill="both")
    # ----------------------------------------------------------------------------------------
    name_label = ttk.Label(input_frame, text="Enter Location where you are planning to start business:",
                           style='Custom.TLabel')
    name_label.grid(row=0, column=0, pady=(0, 10), padx=(0, 10), )
    location_String = tkinter.StringVar()
    location_entry = tkinter.Entry(
        input_frame, width=50, textvariable=location_String)
    location_entry.grid(row=0, column=1)
    location_entry.focus()
    # ----------------------------------------------------------------------------------------
    name_label2 = ttk.Label(
        input_frame, text="Type of Business you are interested in :", style='Custom.TLabel')
    name_label2.grid(row=1, column=0, pady=(0, 10), padx=(0, 10))
    type1_String = tkinter.StringVar()
    type1_entry = tkinter.Entry(
        input_frame, width=50, textvariable=type1_String)
    type1_entry.grid(row=1, column=1, pady=(0, 10))
    # ----------------------------------------------------------------------------------------
    '''
    option1st_button = ttk.Button(root, text="1. Get list of similar business in area", command=Option1st)
    # option1st_button.pack(side="left",fill="x",expand=True)
    option1st_button.pack(side="left")
    quit_button = ttk.Button(root, text="Close the App", command=root.destroy)
    quit_button.pack()'''
    style = ttk.Style()
    style.configure('Custom.TFrame', background='#ffbf00')
    button_frame = ttk.Frame(root, style='Custom.TFrame')
    option1st_button = ttk.Button(button_frame, text="2. Find if the location is suitable",
                                  command=Option2nd)
    option1st_button.pack(side="left", fill="x", expand=True, padx=(0, 10))
    # ----------------------------------------------------------------------------------------

    def des():
        root.destroy()
    quit_button = ttk.Button(button_frame, text="Close the App", command=lambda: [
                             des(), User_Choice()])
    quit_button.pack(fill="x", expand=True)
    button_frame.pack(side="top", pady=(10, 0))

    root.mainloop()


def near_Bus():
    root = Tk()
    root.title('Finding-Business.io')
    root.geometry('800x600')
    root['bg'] = '#ffbf00'
    style = ttk.Style()
    style.configure('Custom.TLabel', background='#ffbf00')
    # style= ttk.Style()
    style.configure('Custom.TLabel1', background='#87cefa')

    # --------------------------------------------------------------------------------------------

    def Option1st():
        location = location_String.get()
        type1 = type1_String.get()
        api_file = open("shubham_api_key.txt", "r")
        from prettytable import PrettyTable
        x = PrettyTable()
        x.field_names = ["Business", "Address"]
        api_key = api_file.read()
        api_file.close()
        import googlemaps
        gmaps = googlemaps.Client(api_key)
        geocode_result = gmaps.geocode(location)
        if not geocode_result:
            print("No results found for the entered location.")

        else:
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            places_result = gmaps.places_nearby(
                location=(lat, lng), radius=500, type=type1)
            canvas = tkinter.Canvas(root)
            canvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            scrollbar = ttk.Scrollbar(
                root, orient=tkinter.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            canvas.configure(yscrollcommand=scrollbar.set)
            inner_frame = tkinter.Frame(canvas)
            canvas.create_window((0, 0), window=inner_frame, anchor=tkinter.NW)
            output_treeview = ttk.Treeview(inner_frame)
            output_treeview['columns'] = ('Column 1', 'Column 2')
            # output_treeview.heading('#0', text='Item')
            output_treeview.heading('Column 1', text='Business Name')
            output_treeview.heading('Column 2', text='Address')
            serial_numbering = 0
            for place in places_result['results']:
                serial_numbering += 1
                # dict_for_output[place['name']]=place['vicinity']
                output_treeview.insert(parent='', index='end', text=serial_numbering,
                                       values=(place['name'], place['vicinity']))
                # output_treeview.insert(parent='', index='end', text='Item 2', values=('Value 3', 'Value 4'))
            output_treeview.grid(row=1, column=0, sticky="nsew")
            inner_frame.bind('<Configure>', lambda event: canvas.configure(
                scrollregion=canvas.bbox('all')))

    # ------------------------------------------------------------------------------------------
    t = ttk.Label(root, text="Welcome to Finding-Business.io",
                  font=50, style='Custom.TLabel')
    t.pack()
    t = ttk.Label(root, text="With our software you can find the perfect location to start your new business.",
                  padding=(30, 10), style='Custom.TLabel')
    t.pack()
    # ----------------------------------------------------------------------------------------
    input_frame = ttk.Frame(root, padding=(
        20, 10, 20, 0), style='Custom.TLabel')
    input_frame.pack(fill="both")
    # ----------------------------------------------------------------------------------------
    name_label = ttk.Label(input_frame, text="Enter Location where you are planning to start business:",
                           style='Custom.TLabel')
    name_label.grid(row=0, column=0, pady=(0, 10), padx=(0, 10), )
    location_String = tkinter.StringVar()
    location_entry = tkinter.Entry(
        input_frame, width=50, textvariable=location_String)
    location_entry.grid(row=0, column=1)
    location_entry.focus()
    # ----------------------------------------------------------------------------------------
    name_label2 = ttk.Label(
        input_frame, text="Type of Business you are interested in :", style='Custom.TLabel')
    name_label2.grid(row=1, column=0, pady=(0, 10), padx=(0, 10))
    type1_String = tkinter.StringVar()
    type1_entry = tkinter.Entry(
        input_frame, width=50, textvariable=type1_String)
    type1_entry.grid(row=1, column=1, pady=(0, 10))
    # ----------------------------------------------------------------------------------------

    option1st_button = ttk.Button(
        root, text="1. Get list of similar business in area", command=Option1st)
    # option1st_button.pack(side="left",fill="x",expand=True)
    option1st_button.pack()

    def des():
        root.destroy()
    quit_button = ttk.Button(root, text="Close the App",
                             command=lambda: [des(), User_Choice()])
    quit_button.pack()
    root.mainloop()


def User_Choice():
    T = Tk()
    T.geometry("600x300")

    def des():
        T.destroy()
    T.title("USER CHOICE")
    global L4, Bu1, Bu2
    photoback = PIL.Image.open("back.png")
    photo2 = ImageTk.PhotoImage(photoback)
    L4 = tkinter.Label(image=photo2)
    L4.image = photo2
    L4.pack()
    Bu1 = Button(T, text="1. Search Similar Business", command=lambda: [des(), near_Bus(
    )], bg="#7FFFD4", font=("Algerian", 15), bd=5, activebackground="#00BFFF")
    Bu1.place(x=20, y=50)
    Bu2 = Button(T, text="2. CHECK POPULARITY OF LOCATION", command=lambda: [
                 des(), review()], bg="#7FFFD4", font=("Algerian", 15), bd=5, activebackground="#00BFFF")
    Bu2.place(x=60, y=110)
    Bu3 = Button(T, text="3. ANALYSE PUBLIC TRANSPORTATION", command=lambda: [des(), transport()],
                 bg="#7FFFD4", font=("Algerian", 15), bd=5, activebackground="#00BFFF")
    Bu3.place(x=100, y=170)
    quit_button = ttk.Button(T, text="Close the App", command=T.destroy)
    quit_button.pack()
    quit_button.place(x=250, y=220)

    T.mainloop()


def mainscreen():
    T = Tk()
    T.geometry("600x300")

    def des():
        T.destroy()
    T.title("FIND MY BUSINESS")
    photoback = PIL.Image.open("back.png")
    photo2 = ImageTk.PhotoImage(photoback)
    L4 = tkinter.Label(image=photo2)
    L4.image = photo2
    L4.pack()
    photoback = PIL.Image.open("topic.png")
    photo2 = ImageTk.PhotoImage(photoback)
    L4 = tkinter.Label(image=photo2, bd=0)
    L4.image = photo2
    L4.place(x=20, y=20)

    image2 = PhotoImage(file="button.png")
    Bu1 = Button(T, image=image2, text="Lets Start", command=lambda: [des(), User_Choice(
    )], bg="#3709ff", font=("Arial", 20), bd=5, activebackground="#3709ff")
    Bu1.place(x=425, y=210)
    T.configure(bg="#67d6f1")

    T.mainloop()


mainscreen()
