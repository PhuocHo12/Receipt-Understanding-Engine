import json
import paho.mqtt.client as mqtt
from src.messaging.redis_queue import RedisQueue


queue = RedisQueue()


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT")
    client.subscribe("receipt/upload")


def on_message(client, userdata, msg):

    payload = json.loads(msg.payload.decode())

    print("Received receipt task")

    queue.push(payload)


def start_mqtt():

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883)

    client.loop_forever()