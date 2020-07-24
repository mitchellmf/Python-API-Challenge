# Section 1: All imports.
import requests
import json
from weather_config import api_key
from pprint import pprint
from pprint import pprint
import random as rd
from citipy import citipy
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# Section 2A: Initialize all lists.
lats = []
lons = []
temps = []
humids = []
clouds = []
winds = []
cities = []
countries = []

# Section 2B: Select 500 random cities using citipy. Then find the weather variables for each of those cities from openweathermap.org.
for i in range(0, 800):
    lat = rd.randrange(-9000,9000) / 100
    lon = rd.randrange(-18000,18000) / 100
    city = citipy.nearest_city(lat, lon)
    city_name = city.city_name
    country = city.country_code
    if city_name not in cities:
        lats.append(lat)
        lons.append(lon)
        cities.append(city_name)
        countries.append(country)    
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        resp_json = response.json()
        #city_name = resp_json['city']['name']
        #country = resp_json['city']['country']
        temp = round((resp_json['current']['temp'] - 273) * 1.8 + 32,2)
        humid = resp_json['current']['humidity']
        cloud = resp_json['current']['clouds']
        wind = resp_json['current']['wind_speed']
        temps.append(temp)
        humids.append(humid)
        clouds.append(cloud)
        winds.append(wind)
print(len(lats))
print(len(lons))
print(len(temps))
print(len(humids))
print(len(clouds))
print(len(winds))
print(len(cities))
print(len(countries))

# Section 3: Compile the individual weather variable lists into one data frame.
weather_dict = {
    'city' : cities ,
    'country' : countries ,
    'lat' : lats ,
    'lon' : lons ,
    'temp' : temps ,
    'humid' : humids ,
    'clouds' : clouds ,
    'winds' : winds    }
weather_df = pd.DataFrame(weather_dict)
print(weather_df.head())


# Section 4: Create the four Scatter Plots that compare latitude against the four weather variables.
plt.scatter( weather_df['lat'] , weather_df['temp'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Temperature")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_temp.png")

plt.scatter( weather_df['lat'] , weather_df['humid'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Humidity")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_humid.png")

plt.scatter( weather_df['lat'] , weather_df['clouds'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Clouds")
plt.xlabel("Latitude")
plt.ylabel("Cloud Cover (%)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_clouds.png")

plt.scatter( weather_df['lat'] , weather_df['winds'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Wind Speed")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_winds.png")

# Section 5A: Divide the data frame into two data frames based on Northern and Southern hemispheres.
weather_df_NH = weather_df.loc[(weather_df['lat'] > 0)]
weather_df_SH = weather_df.loc[(weather_df['lat'] < 0)]


# Create the eight Scatter Plots that compare latitude against the four weather variables, for the Northern and Southern hemispheres.
# Section 5B: The next four scatter plots are for the Northern hemisphere.
plt.scatter( weather_df_NH['lat'] , weather_df_NH['temp'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Temperature in the Northern Hemisphere")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_temp_NH.png")


plt.scatter( weather_df_NH['lat'] , weather_df_NH['humid'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Humidity in the Northern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_humid_NH.png")

plt.scatter( weather_df_NH['lat'] , weather_df_NH['clouds'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Cloud Cover in the Northern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Clouds Cover (%)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_clouds_NH.png")

plt.scatter( weather_df_NH['lat'] , weather_df_NH['winds'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Wind Speed in the Northern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_winds_NH.png")

# Section 5C: The next four scatter plots are for the Southern hemisphere.
plt.scatter( weather_df_SH['lat'] , weather_df_SH['temp'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Temperature in the Southern Hemisphere")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_temp_SH.png")

plt.scatter( weather_df_SH['lat'] , weather_df_SH['humid'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Humidity in the Southern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_humid_SH.png")

plt.scatter( weather_df_SH['lat'] , weather_df_SH['clouds'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Cloud Cover in the Southern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Clouds Cover (%)")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_clouds_SH.png")

plt.scatter( weather_df_SH['lat'] , weather_df_SH['winds'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Wind Speed in the Southern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed")
plt.show()
plt.savefig("C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW6 - APIs\Figures\lat_winds_SH.png")

# Section 6A: Linear regression for latitude vs. temperature, for Northern and Southern hemispheres.
tempNH_slope, tempNH_int, tempNH_r, tempNH_p, tempNH_std_err = stats.linregress( weather_df_NH['lat'] , weather_df_NH['temp'] )
tempSH_slope, tempSH_int, tempSH_r, tempSH_p, tempSH_std_err = stats.linregress( weather_df_SH['lat'] , weather_df_SH['temp'] )
tempNH_fit = tempNH_slope * weather_df_NH['lat'] + tempNH_int
tempSH_fit = tempSH_slope * weather_df_SH['lat'] + tempSH_int

# Section 6B: Plot of latitude vs. temperature in the Northern hemisphere with linear regression superimposed.
plt.scatter( weather_df_NH['lat'] , weather_df_NH['temp'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Temperature in the Northern Hemisphere")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.plot( weather_df_NH['lat'] , tempNH_fit,"--")
plt.show()
print(f"R-squared = {round(tempNH_r**2,2)}")

# Section 6C: Plot of latitude vs. temperature in the Southern hemisphere with linear regression superimposed.
plt.scatter( weather_df_SH['lat'] , weather_df_SH['temp'] , marker="o", facecolors="blue", edgecolors="red")
plt.title("Latitude vs. Temperature in the Southern Hemisphere ")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.plot( weather_df_SH['lat'] , tempSH_fit,"--")
plt.show()
print(f"R-squared = {round(tempSH_r**2,2)}")


