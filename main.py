import phonenumbers
from colorama import Fore, Style, init
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode
from art import *
import datetime
import time
from gps import gps_locator
from domain import is_reg
from domain import ip
init()

def phone():
    from phonenumbers import geocoder
    print(Fore.GREEN+'\n---------------PhoneNumber Info---------------\n'+Style.RESET_ALL)
    key = '8acc2885d0f04bce8fabe50862111d80'
    print("Phone with country code ex:(+919876543210)")
    number = input("Enter the Phone Number:")
    check_num = phonenumbers.parse(number)
    num_location = geocoder.description_for_number(check_num,'en')
    print(time.ctime(),end='\n')
    print("Country:",num_location)

    service_provider = phonenumbers.parse(number)
    servc = carrier.name_for_number(service_provider,'en')
    print("Service  Provider:",servc)

    geocoder = OpenCageGeocode(key)
    query = str(num_location)
    results = geocoder.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    print('Latitude:',lat,'\nLongatitude:',lng,end='\n')

    map_location = folium.Map(location= [lat,lng], zoom_start=9)
    folium.Marker([lat,lng], popup=num_location).add_to(map_location)
    map_location.save("mylocation.html")




if __name__ == '__main__':

    while True:
        tprint('\nINFO-GATHER\n')
        print(Fore.GREEN+"1.PhoneNumber Info...\n"+Style.RESET_ALL)
        print(Fore.GREEN+"2.GPS Info...\n"+Style.RESET_ALL)
        print(Fore.GREEN+"3.Domain Info...\n"+Style.RESET_ALL)
        print(Fore.GREEN+"4.IP Info...\n"+Style.RESET_ALL)
        print(Fore.GREEN+"5.Exit...\n"+Style.RESET_ALL)

    
        inp = int(input("Enter the Value:"))

        if inp == 1:
            phone()
            
        elif inp == 2:
            print(Fore.GREEN+'\n---------------GPS Info---------------\n'+Style.RESET_ALL)
            page = gps_locator()
            
        elif inp == 3:
            print(Fore.GREEN+'\n---------------Domain Info---------------\n'+Style.RESET_ALL)
            d_name = input("Enter the domain name:")
            is_reg(d_name)
            
        elif inp == 4:
            print(Fore.GREEN+'\n---------------IP Info---------------\n'+Style.RESET_ALL)
            ip_add = input("Enter the IP Address:")
            ip(ip_add)

        elif inp == 5:
            break
        else:
            print(Fore.GREEN+"Invalid Input...\n"+Style.RESET_ALL)
            continue
           
        ac = input(Fore.GREEN+"Do you  want to continue? (y/n):"+Style.RESET_ALL)
        if ac.lower() == 'n':
            break
        else:
            continue

