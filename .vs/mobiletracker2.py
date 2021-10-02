import csv
import phonenumbers
import possible as possible
from phonenumbers import geocoder ,timezone,carrier
from opencage.geocoder import OpenCageGeocode
import folium
#file handeling,student_info.csv is name of file and w+ indicates write mode,newline puts each new info into separate line a=append so all entries are appended



def write_into_csv(info_list):
    with open('phonenum_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        #csv_file.tell()==0 is to tell the writer write row func to run only if the file is empty
        if csv_file.tell()==0:
             #for header,[] necessary but runs after every input
             writer.writerow(["Phonenumber","Carrier", "Region", "Timezone", "Latitude","Longitude"])
#Program Entry point
if __name__ == "__main__":
    condition = True
    phone_num = 1
    # taking input
    #def phonenum(args):

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

        while (condition):
            phonenum_info_list = input(
                "Enter student information for student #{} in the following format (Name Age Contact_Number Email_ID): "
                .format( phone_num))


    else:
        print("Try again with a valid phone number")
 phonenum_info_list = phonenum_info_list.split(' ')
 # formatted representation for better user experience
 print("\nThe received information is -\nPhonenumber: \nCarrier: {}\nRegion: {}\nTimezone: {}\nLatitude: {}\nLongitude: {}"
      .format(phonenum_info_list[0], phonenum_info_list[1], phonenum_info_list[2], phonenum_info_list[3], phonenum_info_list[4], phonenum_info_list[5] ))
choice_check = input("Is that the information you wanted?(yes/no): ")
if choice_check == "yes":

        # put splited info into write function
        write_into_csv(phonenum_info_list)
        # to continue the computer asks if u want to enter more info
        condition_check = input("Enter yes/no if u want to enter another number: ")

        if condition_check == "yes":
            condition = True
            # since user continues,student number is incremented
            phone_num = phone_num + 1
        elif condition_check == "no":
            condition == False
    elif choice_check == "no":
      phone_num = input("Enter a phone number")
      phone_number = phonenumbers.parse(phone_num)

    # validate number
      valid = phonenumbers.is_valid_number(phone_number)
      possible = phonenumbers.is_possible_number(phone_number)