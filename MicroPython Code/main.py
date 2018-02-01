import time
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.writeto(64, bytearray([0xF5]))
time.sleep_ms(100)
data = i2c.readfrom(64,2)
humid= int.from_bytes(data, 'big')
print(humid)

i2c.writeto(64, bytearray([0xF3]))
time.sleep_ms(100)
data = i2c.readfrom(64,2)
temp = int.from_bytes(data, 'big')
print(temp)

book = {}

book['r1'] = {
    'humidity': humid,
    'temperature': temp,
}

import ujson

payload = ujson.dumps(book)

import network
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')

while (not sta_if.isconnected()):
    pass

print('connected')

from umqtt.simple import MQTTClient

client = MQTTClient('machine.unique_id()','192.168.0.10')
client.connect()
client.publish('esys/KANYE2020/yeezy',bytes(payload,'utf-8'))

