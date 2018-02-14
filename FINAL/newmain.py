import network
import machine
import micropython
import time
from umqtt.simple import MQTTClient
import Medicine
import ujson


p12 = machine.Pin(12)
pwm12 = machine.PWM(p12)
p13 = machine.Pin(13)
pwm13 = machine.PWM(p13)
p14 = machine.Pin(14)
pwm14 = machine.PWM(p14)
p15 = machine.Pin(15)
pwm15 = machine.PWM(p15)


#OUTPUT GREEN
pwm12.freq(50) 
pwm12.duty(0)
pwm13.freq(50) 
pwm13.duty(1023)
pwm14.freq(50) 
pwm14.duty(1023)

#Connect to WIFI
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')
while (not sta_if.isconnected()):
    pass
print('connected')

def sub_cb(topic, msg):
    #print((topic, msg))
    parsed = ujson.loads(msg)
    print(str(parsed))
    if (parsed["Sensor Readings"]["Medicine"] == "Insulin"):
        maxtemp = Medicine.Insulin.MaxTemp()
        mintemp = Medicine.Insulin.MinTemp()
        maxhum = Medicine.Insulin.MaxHum()
        maxvib = Medicine.Insulin.MaxVib()
        realtemp = parsed["Sensor Readings"]["Temperature"]
        realhum = parsed["Sensor Readings"]["Humidity"]
        realx = parsed["Sensor Readings"]["x"]
        realy = parsed["Sensor Readings"]["y"]
        realz = parsed["Sensor Readings"]["z"]
        if ((realtemp > maxtemp) or (realtemp < mintemp)):
            pwm12.freq(50) 
            pwm12.duty(1023)
            pwm13.freq(50) 
            pwm13.duty(1023)
            pwm14.freq(50) 
            pwm14.duty(0)
        elif(realhum > maxhum):
            pwm12.freq(50) 
            pwm12.duty(1023)
            pwm13.freq(50) 
            pwm13.duty(1023)
            pwm14.freq(50) 
            pwm14.duty(0)
        elif(realx > 2000):
            pwm15.freq(587) 
            pwm15.duty(512)
            time.sleep(0.4)
                
            pwm15.freq(698)
            time.sleep(0.15)
                
            pwm15.freq(880)
            time.sleep(0.15)
                
            pwm15.freq(698)
            time.sleep(0.15)
                
            pwm15.freq(784)
            time.sleep(0.4)
                
            pwm15.freq(880)
            time.sleep(0.15)
                
            pwm15.freq(784)
            time.sleep(0.15)

            pwm15.freq(698)
            time.sleep(0.15)

            pwm15.freq(659)
            time.sleep(0.4)

            pwm15.freq(587)
            time.sleep(0.15)

            pwm15.freq(523)
            time.sleep(0.15)

            pwm15.freq(440)
            time.sleep(0.15)

            pwm15.freq(587)
            time.sleep(0.4)

            pwm15.duty(0)
        else:
            pwm12.freq(50) 
            pwm12.duty(0)
            pwm13.freq(50) 
            pwm13.duty(1023)
            pwm14.freq(50) 
            pwm14.duty(1023)

            
    elif (parsed["Sensor Readings"]["Medicine"] == "IVF"):
        maxtemp = Medicine.IVF.MaxTemp()
        mintemp = Medicine.IVF.MinTemp()
        maxhum = Medicine.IVF.MaxHum()
        maxvib = Medicine.IVF.MaxVib()
        realtemp = parsed["Sensor Readings"]["Temperature"]
        realhum = parsed["Sensor Readings"]["Humidity"]
        realx = parsed["Sensor Readings"]["x"]
        realy = parsed["Sensor Readings"]["y"]
        realz = parsed["Sensor Readings"]["z"]
        if ((realtemp > maxtemp) or (realtemp < mintemp)):
            pwm12.freq(50) 
            pwm12.duty(1023)
            pwm13.freq(50) 
            pwm13.duty(1023)
            pwm14.freq(50) 
            pwm14.duty(0)
        elif(realhum > maxhum):
            pwm12.freq(50) 
            pwm12.duty(1023)
            pwm13.freq(50) 
            pwm13.duty(1023)
            pwm14.freq(50) 
            pwm14.duty(0)
        elif(realx > 2000):
            pwm15.freq(587) 
            pwm15.duty(512)
            time.sleep(0.4)
                
            pwm15.freq(698)
            time.sleep(0.15)
                
            pwm15.freq(880)
            time.sleep(0.15)
                
            pwm15.freq(698)
            time.sleep(0.15)
                
            pwm15.freq(784)
            time.sleep(0.4)
                
            pwm15.freq(880)
            time.sleep(0.15)
                
            pwm15.freq(784)
            time.sleep(0.15)

            pwm15.freq(698)
            time.sleep(0.15)

            pwm15.freq(659)
            time.sleep(0.4)

            pwm15.freq(587)
            time.sleep(0.15)

            pwm15.freq(523)
            time.sleep(0.15)

            pwm15.freq(440)
            time.sleep(0.15)

            pwm15.freq(587)
            time.sleep(0.4)

            pwm15.duty(0)
        else:
            pwm12.freq(50) 
            pwm12.duty(0)
            pwm13.freq(50) 
            pwm13.duty(1023)
            pwm14.freq(50) 
            pwm14.duty(1023)

            
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

#startuptune guest dj Big Patrick
pwm15.freq(587) 
pwm15.duty(512)
time.sleep(0.4)
    
pwm15.freq(698)
time.sleep(0.15)
    
pwm15.freq(880)
time.sleep(0.15)
    
pwm15.freq(698)
time.sleep(0.15)
    
pwm15.freq(784)
time.sleep(0.4)
    
pwm15.freq(880)
time.sleep(0.15)
    
pwm15.freq(784)
time.sleep(0.15)

pwm15.freq(698)
time.sleep(0.15)

pwm15.freq(659)
time.sleep(0.4)

pwm15.freq(587)
time.sleep(0.15)

pwm15.freq(523)
time.sleep(0.15)

pwm15.freq(440)
time.sleep(0.15)

pwm15.freq(587)
time.sleep(0.4)

pwm15.duty(0)

if __name__ == "__main__":
    main()
