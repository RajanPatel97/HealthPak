import machine
import time
import ssd1306
import ujson
import network

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

button1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button2= machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

fini  = 0
while(fini == 0):

    print(button1.value())
    print(button2.value())
   
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

    #elif button3.value():
     #   medicine = "Custom"
      #  iTemp = 
       # fini =1

    time.sleep(1)

Medichoice = {}

#Create Dictionary of Readings
Medichoice['Choice'] = {
    'Medicine': medicine,
    }

#Publish Dictionary as JSONs
payload = ujson.dumps(Medichoice)
client.publish('esys/KANYE2020/yeezys1',bytes(payload,'utf-8'))
