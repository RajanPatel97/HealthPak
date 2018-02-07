# IoT-Product #KANYE2020
Embedded Systems Coursework 1
[airee](https://airee.carrd.co/)

## Product Overview
Detects air quality characteristics such as humidity and air tempreture. The device connects to a broker via WiFi, takes readings and relays this information to a broker which updates live statistics on our website as well as outputting a report on the last hour.

## Instructions
1. Use ampy to load the firmware onto the board: sudo ampy -port COM3 -b 115200 put main.py 
*The put command loads the program onto the board but doesn't run it*

2. Connect your computer to the appropriate broker's network, then intialise the board and turn on the sensor with: python main.py (needs some changes)

3. The program will automatically display and update a live temperature and humidity over time graph.

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
## Team
* Mikhail Demtchenko
* Rajan Patel
* Patrick Reich
* Eliot Makabu
## Website and Contact
[airee](https://airee.carrd.co/) ##link files or get domain
[Email us](md5315@ic.ac.uk)
