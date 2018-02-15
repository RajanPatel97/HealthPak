import ujson
import time
import utime
import network
import ssd1306
import machine
import micropython
import Tmp007
import Si7021
import LIS3DH

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

#Set up I2C Pins
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(15), machine.Pin(0), machine.Pin(16))

oled.fill(0)
oled.text('(1)', 0, 0)
oled.text('Insulin', 20, 0)
oled.text('(2)', 0, 10)
oled.text('IVF', 20, 10)
oled.text('(3)' , 0, 20)
oled.text('Custom Entry', 20, 20)
oled.show()
time.sleep(1)

button1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button2= machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button3= machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

maxtemp = 0
mintemp = 0
maxhum = 0
maxvib = 0

fini  = 0
while(fini == 0):

    print(button1.value())
    print(button2.value())
    print(button3.value())

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
        time.sleep(5)
        medicine = "Custom"
        leave = 0
        oled.fill(0)
        oled.text('MAX TEMPERATURE:', 0, 0)
        maxtemp = 0
        oled.text(str(maxtemp), 64, 10)
        oled.show()
        time.sleep(2)
        print(button1.value())
        print(button2.value())
        print(button3.value())
        while (leave == 0):  
            if not button1.value():
                maxtemp = maxtemp + 1
            if not button2.value():
                maxtemp = maxtemp - 1
            if not button3.value():
                leave = 1
            oled.fill(0)
            oled.text('MAX TEMPERATURE:', 0, 0)
            oled.text(str(maxtemp), 64, 10)
            oled.show()
            time.sleep(2)
        leave1 = 0
        while (leave1 == 0):  
            oled.fill(0)
            oled.text('MIN TEMPERATURE:', 0, 0)
            mintemp = 0
            oled.text(str(mintemp), 64, 10)
            oled.show()
            if not button1.value():
                mintemp = mintemp + 1
            if not button2.value():
                mintemp = mintemp - 1
            if not button3.value():
                leave1 = 1
        leave2 = 0
        while (leave2 == 0):  
            oled.fill(0)
            oled.text('MAX HUMIDITY:', 0, 0)
            maxhum = 0
            oled.text(str(maxhum), 64, 10)
            oled.show()
            if not button1.value():
                maxhum = maxhum + 1
            if not button2.value():
                maxhum = maxhum - 1
            if not button3.value():
                leave2 = 1
        leave3 = 0
        while (leave3 == 0):  
            oled.fill(0)
            oled.text('MAX VIBRATION:', 0, 0)
            maxvib = 0
            oled.text(str(maxvib), 64, 10)
            oled.show()
            if not button1.value():
                maxvib = maxvib + 1
            if not button2.value():
                maxvib = maxvib - 1
            if not button3.value():
                leave3 = 1
        oled.fill(0)
        oled.text('SELECTION SAVED', 0, 0)
        oled.show()

        fini = 1
    time.sleep(0.5)

# Instantiate Sensors
tempSensor = Tmp007.TMP007(i2c, TEMP007ADR)
si7021Sensor = Si7021.Si7021(i2c, SI7021ADR)
lis3dhSensor = LIS3DH.lis3dh(i2c, LIS3DHADR)

Readings = {}

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
        #'Custom': {
         #   'MaxTemp': = maxtemp,
          #  'MinTemp': = mintemp,
           # 'MaxHum': = maxhum,
            #'MaxVib': = maxVib,
        #}
    }

    #Publish Dictionary as JSONs
    payload = ujson.dumps(Readings)
    client.publish('esys/KANYE2020/yeezy',bytes(payload,'utf-8'))
    time.sleep(5)
