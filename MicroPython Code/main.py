import ujson
import time
import utime
import network
import ssd1306
import machine



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

Readings = {}

n = 0

while True:

    i2c.writeto(64, bytearray([0xF5]))
    time.sleep_ms(20)
    data = i2c.readfrom(64,2)
    humidcode= int.from_bytes(data, 'big')
    humid = float(((125*humidcode)/65536) - 6)


    i2c.writeto(64, bytearray([0xF3]))
    time.sleep_ms(20)
    data = i2c.readfrom(64,2)
    tempcode = int.from_bytes(data, 'big')
    temp = float(((175.72*tempcode)/65536) - 46.85)
    
    co2data = open('co2.txt') 
    co2code = co2data.read().split("\n") 
    tvocdata = open('tvoc.txt') 
    tvoccode = tvocdata.read().split("\n") 

    if n == 100:
        n = 0
    n = n + 1
    co2 = co2code[n]
    tvoc = co2code[n]

    humidity = str(humid)
    temperature = str(temp)
    co2disp = str(co2)
    tvocdisp = str(tvoc)
    
    

    oled.fill(0)
    oled.text('Temp (C)', 0, 0)
    oled.text(temperature, 70, 0)
    oled.text('Hum (%)', 0, 10)
    oled.text(humidity, 70, 10)
    oled.text('CO2(ppm)' , 0, 20)
    oled.text(co2disp, 70, 20)
    oled.show()
    
    
    timestamp = utime.localtime()

    print("Temperature(C):",  temp)
    print("Humidity(%):", humid)
    print("Time(s):", timestamp)
    
    Readings['Sensor Readings'] = {
        'Time': timestamp,
        'Temperature': temp,
        'Humidity': humid,
        'CO2': co2,
        'tVOC': tvoc,
    }
    payload = ujson.dumps(Readings)
    client.publish('esys/KANYE2020/yeezy',bytes(payload,'utf-8'))
    time.sleep(5)
