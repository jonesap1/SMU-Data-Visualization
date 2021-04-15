# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress
import json

# Import API key
from api_keys import weather_api_key
API_KEY=weather_api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(len(cities))
totcitydata=(len(cities))
if len(cities)>500:
    print("Okay to Proceed")
else:
    print("Need More City Data")
l = "http://api.openweathermap.org/data/2.5/weather?"
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + API_KEY
response = requests.get(f"{url}&q={city}").json() 
response

#Json weather check for each city and print log
city_name = []
clouds = []
country = []
wind_speed = []
date = []
latitude = []
longitude = []
max_temp = []
humidity = []

counter=1
print(f"Weather Data Processing Initialization")
print(f"______________________________________")
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + API_KEY
for city in cities:
    try:
        response=requests.get(f"{url}&q={city}").json()
        city_name.append(response["name"])
        clouds.append(response["clouds"]["all"])
        country.append(response["sys"]["country"])
        date.append(response["dt"])
        humidity.append(response["main"]["humidity"])
        max_temp.append(response["main"]["temp_max"])
        latitude.append(response["coord"]["lat"])
        longitude.append(response["coord"]["lon"])
        wind_speed.append(response["wind"]["speed"])
        city_record = response["name"]
        print(f"Processing Record {counter} of {totcitydata} | {city_record}")
        counter=counter+1

# If no record found "skip" to next call
    except:
        print("City not found. Skipping this location...")
    continue