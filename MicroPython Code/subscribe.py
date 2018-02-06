import paho.mqtt.client as mqtt
import json
import time
import matplotlib.pyplot as plt

list1 = []
list2 = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("esys/KANYE2020/#")

def on_message(client, userdata, msg):
     parsed = json.loads(msg.payload)
     list1.append(parsed["Sensor Readings"]["T"]) 
     list2.append(parsed["Sensor Readings"]["H"])

     
     plt.plot(list1)
     plt.ylabel('Temperature(C)')
     plt.xlabel('Readings')
     plt.show()
     
     #print(msg.topic+" "+str(msg.payload))
     #print(str(json.dumps(list)))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.10", 1883, 60)
client.loop_forever()
