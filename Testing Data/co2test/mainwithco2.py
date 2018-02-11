import ujson
import time
import network
import adafruit_ccs811.py

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

Readings = {}

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

    print("Temperature(C):",  temp)
    print("Humidity(%):", humid)
    
    i2c.writeto(64, bytearray([0x5A])) # Could also use 0x5B for low
    time.sleep_ms(20)
    
    #Parameters for CO2 Sensor
    co2_temp  = temp - 273
    co2_humid = humid
    
    #Sensor requires 48 hour burn in to get a baseline value, in absence of sensor we will simulate the baseline
    
    
    data = i2c.readfrom(64,2)
    CO2code= int.from_bytes(data, 'big') #raw data
    #CO2 = float(((125*humidcode)/65536) - 6) #this has to be a difference based calculation, returns IAQ (Indoor Air Quality)
    
    #f = open('data.txt') #test data in absence of sensor

    #co2code = f.read().split("\n") 
    
    #only works if the sensor is attached
    s = CCS811.CCS811()
    time.sleep(1)
    while True:
        if s.data_ready():
            co2 = s.eCO2
            tvoc = s.tVOC
            time.sleep(1)
    
    
    Readings['Sensor Readings'] = {
        'T': temp,
        'H': humid,
        'CO2 ppm': co2,
        'tVOC ppb (mg/m^3)': tvoc
    }
    payload = ujson.dumps(Readings)
    client.publish('esys/KANYE2020/yeezy',bytes(payload,'utf-8'))
    time.sleep(5)
