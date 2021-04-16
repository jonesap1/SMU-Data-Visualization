# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import os
from scipy.stats import linregress
import json
from datetime import datetime
import PIL as PIL

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

url = "http://api.openweathermap.org/data/2.5/weather?"
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

city_data=pd.DataFrame({"City":city_name,
                        "Cloudiness":clouds,
                        "Country":country,
                        "Date":date,
                        "Humidity":humidity,
                        "Lat":latitude,
                        "Lng":longitude,
                        "Max Temp":max_temp,
                        "Wind Speed":wind_speed})
city_data

city_data["Humidity"].max()

city_data.count()

# Make a new DataFrame equal to the city data to drop all humidity outliers by index.
#convert unix timestamp to date time - pandas.pydata.org time series/date functionality
city_data["Date"]=pd.to_datetime(city_data["Date"],unit="s")
# Passing "inplace=False" will make a copy of the city_data DataFrame, which we call "clean_city_data".
clean_city_data=city_data[["City","Lat","Lng","Max Temp","Humidity", "Cloudiness", "Wind Speed", "Country", "Date"]]
clean_sort=clean_city_data.sort_values(by='City',ascending=True).reset_index(drop=True)
clean_sort

clean_sort=clean_sort.rename(columns={"Max Temp":"Max Temp ˚F"})
clean_sort
clean_sort.to_csv('output_data/cities.csv',index=True,header=True)
datadate=((clean_sort.iloc[0,8]))
chartdate=(datadate.strftime("%b %d, %Y"))

plt.scatter(clean_sort["Lat"],clean_sort["Max Temp ˚F"], marker="o", facecolors="lightblue", edgecolors="black",)
plt.title("City Latitude vs. Max. Temperature  "+"("+chartdate+")")
plt.ylabel("Max. Temperature (˚F)")
plt.xlabel("Latitude")
plt.grid()
plt.savefig("output_data/citylatvsmaxtemp.png")
plt.savefig("output_data/Fig1.png")
plt.show()

plt.scatter(clean_sort["Lat"],clean_sort["Humidity"], marker="o", facecolors="lightblue", edgecolors="black",)
plt.title("City Latitude vs. Humidity (%)  "+"("+chartdate+")")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid()
plt.savefig("output_data/citylatvshumidity.png")
plt.savefig("output_data/Fig2.png")
plt.show()

plt.scatter(clean_sort["Lat"],clean_sort["Cloudiness"], marker="o", facecolors="lightblue", edgecolors="black",)
plt.title("City Latitude vs. Cloudiness (%)  "+"("+chartdate+")")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid()
plt.savefig("output_data/citylatvscloud.png")
plt.savefig("output_data/Fig3.png")
plt.show()

plt.scatter(clean_sort["Lat"],clean_sort["Wind Speed"], marker="o", facecolors="lightblue", edgecolors="black",)
plt.title("City Latitude vs. Wind Speed  "+"("+chartdate+")")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid()
plt.savefig("output_data/citylatvsmaxtemp.png")
plt.savefig("output_data/Fig4.png")
plt.show()

northhem=clean_sort[clean_sort['Lat']>=0]
southhem=clean_sort[clean_sort['Lat']<0]

x_values = northhem['Lat']
y_values = northhem['Max Temp ˚F']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")

plt.scatter(northhem["Lat"],northhem["Max Temp ˚F"], marker="o", facecolors="lightblue", edgecolors="black",)
plt.title("Northern Latitude vs. Max. Temperature  "+"("+chartdate+")")
plt.ylabel("Max. Temperature (˚F)")
plt.xlabel("Latitude")
plt.grid()

print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/citynorthlatvsmaxtemp.png")
plt.savefig("output_data/Fig5.png")
plt.show()

x_values = southhem['Lat']
y_values = southhem['Max Temp ˚F']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(-26,50),fontsize=15,color="red")

plt.scatter(southhem["Lat"],southhem["Max Temp ˚F"], marker="o", facecolors="lightblue", edgecolors="black",)
plt.title("Southern Latitude vs. Max. Temperature  "+"("+chartdate+")")
plt.ylabel("Max. Temperature (˚F)")
plt.xlabel("Latitude")
plt.grid()

print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/citynorthlatvsmaxtemp.png")
plt.savefig("output_data/Fig6.png")
plt.show()

x_values = northhem['Lat']
y_values = northhem['Humidity']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values, y_values, marker="o", facecolors="lightblue", edgecolors="black",)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(50,5),fontsize=15,color="red")
plt.title("Northern Latitudes vs. Humidity (%) "+"("+chartdate+")")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid()
print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/northlatvshumidity.png")
plt.savefig("output_data/Fig7.png")
plt.show()

x_values = southhem['Lat']
y_values = southhem['Humidity']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values, y_values, marker="o", facecolors="lightblue", edgecolors="black",)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(50,5),fontsize=15,color="red")


plt.title("Southern Latitudes vs. Humidity (%) "+"("+chartdate+")")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid()
print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/southlatvshumidity.png")
plt.savefig("output_data/Fig8.png")
plt.show()

x_values = northhem['Lat']
y_values = northhem['Cloudiness']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values, y_values, marker="o", facecolors="lightblue", edgecolors="black",)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(50,45),fontsize=15,color="red")
plt.title("Northern Latitudes vs. Cloudiness (%) "+"("+chartdate+")")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid()
print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/northlatvscloudiness.png")
plt.savefig("output_data/Fig9.png")
plt.show()

x_values = southhem['Lat']
y_values = southhem['Cloudiness']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values, y_values, marker="o", facecolors="lightblue", edgecolors="black",)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(50,45),fontsize=15,color="red")
plt.title("Southern Latitudes vs. Cloudiness (%) "+"("+chartdate+")")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid()
print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/southlatvscloudiness.png")
plt.savefig("output_data/Fig10.png")
plt.show()

x_values = northhem['Lat']
y_values = northhem['Wind Speed']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values, y_values, marker="o", facecolors="lightblue", edgecolors="black",)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(0,25),fontsize=15,color="red")
plt.title("Northern Latitudes vs. Windspeed (%) "+"("+chartdate+")")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid()
print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/northlatvsWindspeed.png")
plt.savefig("output_data/Fig11.png")
plt.show()

x_values = southhem['Lat']
y_values = southhem['Wind Speed']
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values, y_values, marker="o", facecolors="lightblue", edgecolors="black",)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(-55,13),fontsize=15,color="red")
plt.title("Southern Latitudes vs. Windspeed (%) "+"("+chartdate+")")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid()
print(f"The r-squared is: {rvalue**2}")
plt.savefig("output_data/southlatvsWindspeed.png")
plt.savefig("output_data/Fig12.png")
plt.show()

from PIL import Image
im1=Image.open("output_data/fig1.png")
im2=Image.open("output_data/fig2.png")
def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst
get_concat_h(im1, im2).save('output_data/fig13.jpg')

im3=Image.open("output_data/fig3.png")
im4=Image.open("output_data/fig4.png")
def get_concat_h(im3, im4):
    dst = Image.new('RGB', (im3.width + im4.width, im3.height))
    dst.paste(im3, (0, 0))
    dst.paste(im4, (im3.width, 0))
    return dst
get_concat_h(im3, im4).save('output_data/fig14.jpg')
im5=Image.open("output_data/fig5.png")
im6=Image.open("output_data/fig6.png")
def get_concat_h(im5, im6):
    dst = Image.new('RGB', (im5.width + im6.width, im5.height))
    dst.paste(im5, (0, 0))
    dst.paste(im6, (im5.width, 0))
    return dst
get_concat_h(im5, im6).save('output_data/fig15.jpg')

im7=Image.open("output_data/fig7.png")
im8=Image.open("output_data/fig8.png")
def get_concat_h(im7, im8):
    dst = Image.new('RGB', (im7.width + im8.width, im7.height))
    dst.paste(im7, (0, 0))
    dst.paste(im8, (im7.width, 0))
    return dst
get_concat_h(im7, im8).save('output_data/fig16.jpg')
im9=Image.open("output_data/fig9.png")
im10=Image.open("output_data/fig10.png")
def get_concat_h(im9, im10):
    dst = Image.new('RGB', (im9.width + im10.width, im9.height))
    dst.paste(im9, (0, 0))
    dst.paste(im10, (im9.width, 0))
    return dst
get_concat_h(im9, im10).save('output_data/fig17.jpg')
im11=Image.open("output_data/fig11.png")
im12=Image.open("output_data/fig12.png")
def get_concat_h(im11, im12):
    dst = Image.new('RGB', (im11.width + im12.width, im11.height))
    dst.paste(im11, (0, 0))
    dst.paste(im12, (im11.width, 0))
    return dst
get_concat_h(im11, im12).save('output_data/fig18.jpg')
im13=Image.open("output_data/fig13.jpg")
im14=Image.open("output_data/fig14.jpg")
def get_concat_h(im13, im14):
    dst = Image.new('RGB', (im13.width + im14.width, im13.height))
    dst.paste(im13, (0, 0))
    dst.paste(im14, (im13.width, 0))
    return dst
get_concat_h(im13, im14).save('output_data/fig19.jpg')
im15=Image.open("output_data/fig15.jpg")
im16=Image.open("output_data/fig16.jpg")
def get_concat_h(im15, im16):
    dst = Image.new('RGB', (im15.width + im16.width, im15.height))
    dst.paste(im15, (0, 0))
    dst.paste(im16, (im15.width, 0))
    return dst
get_concat_h(im15, im16).save('output_data/fig20.jpg')
im17=Image.open("output_data/fig17.jpg")
im18=Image.open("output_data/fig18.jpg")
def get_concat_h(im17, im18):
    dst = Image.new('RGB', (im17.width + im18.width, im17.height))
    dst.paste(im17, (0, 0))
    dst.paste(im18, (im17.width, 0))
    return dst
get_concat_h(im17, im18).save('output_data/fig21.jpg')
im19=Image.open("output_data/fig19.jpg")
im20=Image.open("output_data/fig20.jpg")
def get_concat_v(im19, im20):
    dst = Image.new('RGB', (im19.width, im19.height + im20.height))
    dst.paste(im19, (0, 0))
    dst.paste(im20, (0, im19.height))
    return dst

get_concat_v(im19, im20).save('output_data/fig22.jpg')
im21=Image.open("output_data/fig21.jpg")
im22=Image.open("output_data/fig22.jpg")
def get_concat_v(im22, im21):
    dst = Image.new('RGB', (im22.width, im22.height + im21.height))
    dst.paste(im22, (0, 0))
    dst.paste(im21, (0, im22.height))
    return dst

get_concat_v(im22, im21).save('output_data/fig23.jpg')