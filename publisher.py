import paho.mqtt.client as mqtt
import time
from random import uniform
from datetime import datetime

mqttBroker = "broker.hivemq.com"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    now = datetime.now().time()

    randNumber = uniform(0.0, 100.0)
    kisa_rand = round(randNumber, 3)
    client.publish("TEMPERATURE", kisa_rand)
    print("Just published " + str(kisa_rand) + " to topic ESP/mechine " +
          str(now))
    time.sleep(0.5)
