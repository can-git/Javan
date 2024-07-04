import paho.mqtt.client as mqtt
import time

# MQTT settings
broker = "host.docker.internal"
port = 1883
topic = "sampleTopic"

# Create an MQTT client instance
client = mqtt.Client()

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

# Assign the callback functions
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker, port)

# Start the MQTT client
client.loop_start()

# Publish messages at regular intervals
i = 0
try:
    while True:
        message = i
        result = client.publish(topic, message)

        # Wait for the message to be published
        status = result[0]
        if status == 0:
            print(f"Sent `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

        # Wait for 1 second before publishing the next message
        time.sleep(1)
        i += 1

except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
