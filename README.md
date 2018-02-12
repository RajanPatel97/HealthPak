# IoT-Product #KANYE2020
Embedded Systems Coursework 1
[coldbox](https://airee.carrd.co/)

## Product Overview
Smart cold box that monitors the enviroment inside a cold box allowing safe and intelligent storage and transport of temperature and vibration sensitive goods such as medicines, organs, foods and others. The cold box measures the temperature and humidity of the box, surface temperature of the good and if it has been subject to vibration. The cold box will feed back live characteristics and it will alert you if the thresholds have been exceeded and for how long.

## System Diagram
![Coolerbox](https://github.com/RajanPatel97/IoT-Product/blob/master/Coolerbox.jpg)

## Instructions
1. Use ampy to load the firmware onto the board: `sudo ampy -port COM3 -b 115200 put main.py` 
*The put command loads the program onto the board but doesn't run it*

2. Connect your computer to the appropriate broker's network, then intialise the board and turn on the sensor with: python main.py (needs some changes)

3. Input the parameters required into the menu, this will set the thresholds for alarms. The program will automatically display and update a live temperature and humidity over time graph. 

4. Accessing the website will direct you to an online version of this data, which can be accessed from anywhere, not requiring a constant broker connection for any devices that want to recieve the data.

## Software
* Micropython
* Javascript
### Library
* IFFFT Smart Plug ##possibly
* Si7021-A20 
* [SSD1306](https://raw.githubusercontent.com/adafruit/micropython-adafruit-ssd1306/master/ssd1306.py)
* Chart-JS
* [Adafruit-MQTT](https://github.com/adafruit/Adafruit_MQTT_Library)
## Hardware
* SSD1306 LCD Display Module
* ESP8266 Microcontroller
* Si7021-A20 Temperature and Humidity Sensor 
* TMP007 Infrared Thermopile Sensor
* LIS3DH Accelerometer
* Cooler
## Team
* Mikhail Demtchenko
* Rajan Patel
* Patrick Reich
* Eliot Makabu
## Website and Contact
[coldbox](https://airee.carrd.co/) ##link files or get domain
[Email us](md5315@ic.ac.uk)
