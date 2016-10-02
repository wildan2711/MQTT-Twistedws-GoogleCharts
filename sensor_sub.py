import paho.mqtt.client as mqtt
from twisted.internet import reactor, protocol
from txws import WebSocketFactory
import json

def shiftLeft(list, data):
    tempList = list[1:len(list)]
    tempList.append(data)
    return tempList

counter = 0

class MQTTtoweb(protocol.Protocol):

    def __init__(self):
        global counter
        self.no = counter
        self.plant = []
        counter += 1

    def connectionMade(self):
        self.mqttc = self.startMQTT()

    def connectionLost(self, reason):
        self.mqttc.loop_stop()

    def save(self,data):
        topic = data["topic"].split("/")
        exists = False
        for plant in self.plant:
            if plant["name"] == topic[0]:
                exists = True
                if topic[2] == "temp":
                    plant["temp"] = shiftLeft(plant["temp"], int(data["msg"]))
                elif topic[2] == "humid":
                    plant["humid"] = shiftLeft(plant["humid"], int(data["msg"]))
        if not exists:
            if topic[2] == "temp":
                temp = int(data["msg"])
                humid = 0
            elif topic[2] == "humid":
                temp = 0
                humid = int(data["msg"])
            dict = {
                "name": topic[0],
                "temp": [0, 0, 0, 0, 0, 0, 0, 0, 0, temp],
                "humid": [0, 0, 0, 0, 0, 0, 0, 0, 0, humid]
            }
            self.plant.append(dict)
        print self.no,". "+json.dumps(self.plant)
        self.transport.write(json.dumps(self.plant))

    def onReceive(self,mqttc, obj, msg):
        data = {"topic": msg.topic,
                "msg": msg.payload
                }
        self.save(data)

    def startMQTT(self):
        mqttc = mqtt.Client("sub1", clean_session=False)
        mqttc.on_message = self.onReceive

        mqttc.connect("localhost", 1883)

        mqttc.subscribe("+/sensors/+", qos=0)

        mqttc.loop_start()
        return mqttc


def main():
    factory = protocol.ServerFactory()
    factory.protocol = MQTTtoweb
    reactor.listenTCP(9000, WebSocketFactory(factory))
    reactor.run()

if __name__ == '__main__':
    main()
