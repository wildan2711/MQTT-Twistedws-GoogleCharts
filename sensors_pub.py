import json
import paho.mqtt.client as mqtt
import random, time, threading, sys

if len(sys.argv) == 2:
    plant = sys.argv[1]
else:
    raise Exception("Input a plant")

mqttc = mqtt.Client(plant, clean_session=False)

mqttc.connect("127.0.0.1", 1883)

def pub():
    mqttc.publish(plant+"/sensors/temp", payload=int(random.normalvariate(30,1.5)), qos=0)
    time.sleep(1)
    mqttc.publish(plant+"/sensors/humid", payload=int(random.normalvariate(70,1.5)), qos=0)
    threading.Timer(1, pub).start()

pub()
