Objective: Show on what country the ISS is passing by.

The application will use <b>JSON</b> to pull the current coordinates (latitude,longitude) of the International 
Space Station (ISS).After obtaining the coordinates, it will use <b>geopy.Nominatim</b> to get the geolocation using the 
coordinates. Then will extact only the country name and display it using the sense hat matrix display.

Is the user don't have the sense hat there are two options:
1. The code can be change to only use print and not the matrix display.
2. Use the sense hat emulator included on Raspbian by enabeling the libary <b>from sense_emu import SenseHat</b>.
