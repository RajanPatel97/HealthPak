# IoT-Product #KANYE2020 HEALTHPAK
Embedded Systems Coursework 1

![healhpaklogo](https://github.com/RajanPatel97/IoT-Product/blob/master/HealthPakLogoCut.png)

## Product Overview
Smart cold box that monitors the enviroment inside a cold box allowing safe and intelligent storage and transport of temperature and vibration sensitive goods such as medicines, organs, vaccines and others. The cold box measures the temperature and humidity of the box, surface temperature of the good and if it has been subject to vibration. The cold box will feed back live characteristics and it will alert you to a seperate module if the thresholds have been exceeded. 

## System Diagram
![Coolerbox](https://github.com/RajanPatel97/IoT-Product/blob/master/HealthPak.jpg)

## Instructions
1. In the main cooler, ensure the monitoring board is strapped in at the top, and plugged into power. The device will automatically boot. If any error occurs, use the reset button on the board itself to reboot.

2. Ensure the the alarm board is also plugged into power, and that both boards are connected to the same broker. Proceed by entering the specified medicine on the main board, or inputting custom parameters, setting the thresholds for the alarm.

3. The program will automatically display and update a live temperature, humidity and temperature from the breakout sensor on the stem. It will also automatically parse the data and check if it is exceeding any thresholds alerting you if that becomes the case.

4. Accessing the website will direct you to an online version of this data, including time graph showing you past temperature and humidity changes since the board was turned on.

### Instructions for initialising a new board

1. Plug the ESP8266 modules into your computer and use `sudo ampy --PORT COM(your specific port) put main.py` and repeat for all the necessary files. *the put command just loads the file onto the ESP without running it*  If connecting to a network not used before, the SSID and Password will need to be inputted into the code manually.

2. Use `sudo ampy PORT --COM(your specific port) ls` to list all the files on each ESP and ensure all the files were loaded onto the board correctly. *in-cooler ESP should have main.py, outside of cooler ESP should have Medicine, main.py*

3. You can now reset the two boards, if everything is correct the in-cooler ESP should go to menu and the off-cooler ESP should light up and make a jingle. If it isn't working, restart it again, and if it persists reload the files onto the boards.

4. You can now proceed with the standard instructions.

## Software
* Micropython
* Javascript
### Libraries
* Si7021-A20 
* [SSD1306](https://raw.githubusercontent.com/adafruit/micropython-adafruit-ssd1306/master/ssd1306.py)
* Chart-JS
* [Adafruit-MQTT](https://github.com/adafruit/Adafruit_MQTT_Library)
* LIS3DH
## Hardware
* SSD1306 LCD Display Module
* ESP8266 Microcontroller
* Si7021-A20 Temperature and Humidity Sensor 
* TMP007 Infrared Thermopile Sensor
* LIS3DH Accelerometer
* Cooler/heater (future implementation)
## Team
* Mikhail Demtchenko
* Rajan Patel
* Patrick Reich
* Eliot Makabu
## Contact Us
[Email us](md5315@ic.ac.uk)
