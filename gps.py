
import requests
from selenium import webdriver
import folium
import datetime
import time



def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    
    except:

        print('Internet Not avialable')

        exit()
        return False

def gps_locator():

    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print('You Are in {},{}'.format(city, state))
        print('Your latitude = {} and longitude = {}'.format(lat, long))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        fileName = '/home/charan/Documents/prgms/projects/' + str(datetime.date.today()) + '.html'

        obj.save(fileName)

        return fileName

    except:
        return False



