#This is the main file for the publisher ESP8266 which automatiically runs this code on startup.
#We have two ESP8266's for our product.
#secmain.py is the second main file for the subscribing ESP8266.

import ujson
import time
import utime
import network
import ssd1306
import machine
import micropython
import TMP007
import Si7021
import LIS3DH
import Screen

#Define Constants
TEMP007ADR = (68)
SI7021ADR = (64)
LIS3DHADR = (24)

#Connect to WIFI
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')
while (not sta_if.isconnected()):
    pass
print('connected')

#Connect to MQTT Broker
from umqtt.simple import MQTTClient
client = MQTTClient('machine.unique_id()','192.168.0.10')
client.connect()

#Set up I2C and OLED Pins
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(15), machine.Pin(0), machine.Pin(16))

#Show OLED Menu
Screen.Screen.menu()
time.sleep(1)

#Set up Buttons
button1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button2= machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button3= machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

#Wait for selection by user input on buttons
#To add more medicines or organs etc, just update Medicines class file
#You can also change code below to allow scrollable screen for more option selection
fini  = 0
while(fini == 0):

    if not button1.value():
        medicine = "Insulin"
        oled.fill(0)
        oled.text('INSULIN SELECTED', 0, 0)
        oled.show()
        fini = 1

    elif not button2.value():
        medicine = "IVF"
        oled.fill(0)
        oled.text('IVF SELECTED', 0, 0)
        oled.show()
        fini = 1

    elif not button3.value():
        medicine = "Heart"
        oled.fill(0)
        oled.text('Heart SELECTED', 0, 0)
        oled.show()
        fini = 1
    time.sleep(0.5)

# Instantiate Sensors
tempSensor = TMP007.TMP007(i2c, TEMP007ADR)  #TMP007 Thermopile Sensor
si7021Sensor = Si7021.Si7021(i2c, SI7021ADR) #Si7021 Temp/Humidity Sensor
lis3dhSensor = LIS3DH.lis3dh(i2c, LIS3DHADR) #LIS3DH Accelerometer

Readings = {} #Initialise Dictionary

while True:

    #Get Sensor Readings
    humid = si7021Sensor.ambHum()
    temp = si7021Sensor.ambTemp()
    stemp = tempSensor.objTemp()
    xval = lis3dhSensor.xRead()
    yval = lis3dhSensor.yRead()
    zval = lis3dhSensor.zRead()
    

    #Convert Readings to String for OLED Output
    humidity = str(humid)
    temperature = str(temp)
    sstemp = str(stemp)
    

    #Output Readings to OLED
    oled.fill(0)
    oled.text('Temp (C)', 0, 0)
    oled.text(temperature, 70, 0)
    oled.text('Hum (%)', 0, 10)
    oled.text(humidity, 70, 10)
    oled.text('Stem (C)' , 0, 20)
    oled.text(sstemp, 70, 20)
    oled.show()

    #Get timestamp - use preset time on board
    #Usually initalise with current time but no connection to internet over EEEROVER
    timestamp = utime.localtime()

    #Output Readings to Terminal
    print("Temperature(C):",  temp)
    print("Humidity(%):", humid)
    print("Time(s):", timestamp)
    print("STemp:", sstemp)
    print("Medicine:", medicine)
    print("X:", xval)
    print("Y:", yval)
    print("Z:", zval)

    #Create Dictionary of Readings
    Readings['Sensor Readings'] = {
        'Time': timestamp,
        'Temperature': temp,
        'Humidity': humid,
        'Stemp': stemp,
        'Medicine': medicine,
        'x': xval,
        'y': yval,
        'z': zval,
    }

    #Publish Dictionary as JSON over MQTT
    payload = ujson.dumps(Readings)
    client.publish('esys/KANYE2020/yeezy',bytes(payload,'utf-8'))
    time.sleep(2)
