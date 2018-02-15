#This the main file for the second ESP8266 used for subscribing and outputs.
#It runs automattically on startup and is saved as main.py on the actual chip.
#Saved as secmain.py on github for your convinience

import network
import machine
import micropython
import time
from umqtt.simple import MQTTClient
import Medicine
import ujson
import IO
import CondCheck

#HUMID LED SETUP
p12 = machine.Pin(12)
pwm12 = machine.PWM(p12)
p13 = machine.Pin(13)
pwm13 = machine.PWM(p13)
p14 = machine.Pin(14)
pwm14 = machine.PWM(p14)

#TEMPERATURE LED SETUP
p0 = machine.Pin(0)
pwm0 = machine.PWM(p0)
p5 = machine.Pin(5)
pwm5 = machine.PWM(p5)
p2 = machine.Pin(2)
pwm2 = machine.PWM(p2)

#PEIZO BUZZER OUTPUT
p15 = machine.Pin(15)
pwm15 = machine.PWM(p15)

#OUTPUT BOTH LEDS GREEN
IO.IO.humidledgreen()
IO.IO.templedgreen()

#Connect to WIFI
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')
while (not sta_if.isconnected()):
    pass
print('connected')

#Initialise accelerometer, this may give one false positive reading on startup,
#but is necessary for calibration and the comparisons we make therafter in code.
oldx = 0
oldy = 0
oldz = 0

def sub_cb(topic, msg):
    #need to set oldx,oldy,oldz as global as going to change in this local function
    global oldx,oldy,oldz
    #load json message and print
    parsed = ujson.loads(msg)
    print(str(parsed))

    #check if Insulin chosen, carry out CondCheck if so and recalibrate old values
    if (parsed["Sensor Readings"]["Medicine"] == "Insulin"):
        maxtemp = Medicine.Insulin.MaxTemp()
        mintemp = Medicine.Insulin.MinTemp()
        maxhum = Medicine.Insulin.MaxHum()
        maxvib = Medicine.Insulin.MaxVib()
        CondCheck.CondCheck.Checker(parsed, maxtemp, mintemp, maxhum, maxvib, oldx, oldy, oldz)
        oldx = parsed["Sensor Readings"]["x"]
        oldy = parsed["Sensor Readings"]["y"]
        oldz = parsed["Sensor Readings"]["z"]

    #check if IVF chosen, carry out CondCheck if so and recalibrate old values        
    elif (parsed["Sensor Readings"]["Medicine"] == "IVF"):
        maxtemp = Medicine.IVF.MaxTemp()
        mintemp = Medicine.IVF.MinTemp()
        maxhum = Medicine.IVF.MaxHum()
        maxvib = Medicine.IVF.MaxVib()
        CondCheck.CondCheck.Checker(parsed, maxtemp, mintemp, maxhum, maxvib, oldx, oldy, oldz)
        oldx = parsed["Sensor Readings"]["x"]
        oldy = parsed["Sensor Readings"]["y"]
        oldz = parsed["Sensor Readings"]["z"]
        
    #check if Heart chosen, carry out CondCheck if so and recalibrate old values
    elif (parsed["Sensor Readings"]["Medicine"] == "Heart"):
        maxtemp = Medicine.Heart.MaxTemp()
        mintemp = Medicine.Heart.MinTemp()
        maxhum = Medicine.Heart.MaxHum()
        maxvib = Medicine.Heart.MaxVib()
        CondCheck.CondCheck.Checker(parsed, maxtemp, mintemp, maxhum, maxvib, oldx, oldy, oldz)
        oldx = parsed["Sensor Readings"]["x"]
        oldy = parsed["Sensor Readings"]["y"]
        oldz = parsed["Sensor Readings"]["z"]

#loop the main and setup MQTT configuration connections and subscribe channel           
def main(server="192.168.0.10"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"esys/KANYE2020/yeezy")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

#Start-up song also used as alarm but you can use a simple on-off buzz if you want
IO.IO.startnalarm()

#call main
if __name__ == "__main__":
    main()
