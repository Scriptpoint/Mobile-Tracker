import phonenumbers
from phonenumbers import geocoder ,timezone,carrier
from opencage.geocoder import OpenCageGeocode
import folium


phone_num = input("Enter a phone number")
phone_number = phonenumbers.parse(phone_num)

    # validate number
valid = phonenumbers.is_valid_number(phone_number)
possible = phonenumbers.is_possible_number(phone_number)
        
    # finding numbers carrier,location and time zone
if ((valid and possible) == True):
        Carrier = carrier.name_for_number(phone_number, 'en')
        Region = geocoder.description_for_number(phone_number, 'en')
        Timezone = timezone.time_zones_for_number(phone_number)
        print("The carrier is:", Carrier)
        print("The cell location is:", Region)
        print("The time zone is:", Timezone)

        # get your api key
        key = '22d8f60264fb455aa81b22ff7650a203'
        # instance of opencage geocode
        geocoder = OpenCageGeocode(key)
        query = str(Region)

        Result = geocoder.geocode(query)
        lat = Result[0]['geometry']['lat']
        lng = Result[0]['geometry']['lng']
        print("The latitude and longitude  are:", '[', lat, ',', lng, ']')
        # locating and isolating only lat and long...
        myMap = folium.Map(location=[lat, lng], zoom_start=5)
        folium.Marker([lat, lng], popup=Region).add_to(myMap)

        # saving map to html page
        myMap.save('CodeSpeedy.html')

else:
             print("Try again with a valid phone number")