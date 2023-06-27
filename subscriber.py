import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "lidar/object_detection"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print("Received a message on topic: " + msg.topic)
    # Assuming that message is in json format - convert the message to python dict
    data = json.loads(msg.payload)
    print(data)

def main():
    # Create a MQTT client
    client = mqtt.Client()

    # Assign the callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the Broker
    client.connect(BROKER, PORT, 60)

    # Subscribe to the topic
    client.subscribe(TOPIC)

    # Start the MQTT client
    client.loop_forever()

if __name__ == "__main__":
    main()
