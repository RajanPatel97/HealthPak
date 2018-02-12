import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and

    # reconnect then subscriptions will be renewed.

    client.subscribe("esys/KANYE2020/#")



def on_message(client, userdata, msg):

    print(msg.topic+" "+str(msg.payload))



client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect("192.168.0.10", 1883, 60)

client.loop_forever()