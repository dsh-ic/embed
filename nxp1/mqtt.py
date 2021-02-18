 
import paho.mqtt.client as mqtt

import json
import time

client = mqtt.Client()
client.connect("test.mosquitto.org",port=1883)
def on_message(client, userdata, message):
   print("Received message:{} on topic{}".format(message.payload, message.topic))
   data = json.loads(message.payload)
   return data
client.on_message = on_message
client.subscribe("IC.embedded/Team_ALG/#")

def publish_data(temp,hum,pressure,flower_pot):
  payload=json.dumps({"temp":temp,"humidity":hum,"pressure":pressure,"flowerpot":flower_pot})
  client.publish("IC.embedded/Team_ALG/test",payload)
  #default keep alive is 60s,thus we need at least 1 imformation change between broker and client per minutes#
  
#def receive():
  #data = client.on_message()
  # do we need pi to receive any message from app??
  
  
  
