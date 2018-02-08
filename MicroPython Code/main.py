import ujson
import time
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

oled.fill(0)
oled.text('temp', 0, 0)
oled.text('humid', 0, 10)
oled.show()

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
    
    Readings['Sensor Readings'] = {
        'T': temp,
        'H': humid,        
    }
    payload = ujson.dumps(Readings)
    client.publish('esys/KANYE2020/yeezy',bytes(payload,'utf-8'))
    time.sleep(5)
