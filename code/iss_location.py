import json
import urllib
import geopy
import time
#import sense hat emulator.
#from sense_emu import SenseHat
from sense_hat import SenseHat


sense = SenseHat()
sense.set_rotation(270)
na = "No land"

#set low light and turn the LED lights off
sense.low_light = True 
sense.clear()

while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":
        if event.direction == "middle":
            #A JSON request to retrieve the current longitude and latitude of the international space station (real time)  
            url = "http://api.open-notify.org/iss-now.json"
            response = urllib.request.urlopen(url)
            result = json.loads(response.read())

            #Let's extract the required information
            location =result["iss_position"]
            lat = location["latitude"]
            lon = location["longitude"]

            #Output Coordinates 
            print("\nISS Location:")
            print("Latitude: " + str(lat))
            print("Longitude: " + str(lon))

            #Get geolocation of the ISS
            geolocator = geopy.Nominatim(user_agent="my-application", timeout=3)
            location = geolocator.reverse(str(lat) + "," + str(lon), language='en')

            try:
                address = location.raw['address']
                country = address.get('country', '')
                print(country)
                sense.show_message(country,text_colour=[255, 0, 0])
            except:
                sense.show_message(na,text_colour=[255, 0, 0])
            time.sleep(0.5)
            sense.clear()
