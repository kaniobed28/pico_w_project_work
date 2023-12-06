import paho.mqtt.client as mqtt
import json

import csv

def append_to_csv(file_path, data):

    # Open the CSV file in append mode with newline='' to ensure consistent line endings
    with open(file_path, 'a', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the data to the CSV file
        csv_writer.writerow(data)


# MQTT broker details
broker_address = "broker.hivemq.com"  # Replace with your MQTT broker address
port = 1883  # Default MQTT port

# MQTT topic to subscribe to
topic = "day_temp_humd"  # Replace with your desired topic

# Callback when a message is received
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    payload_with_double_quotes = payload.replace("'", '"')

    try:
        payload = json.loads(payload_with_double_quotes)
        print(f"Received message on topic '{msg.topic}': {payload}")
        # Now you can use data_dict as a regular dictionary
        # append_to_csv('example.csv', data_dict)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    
# Example usage
    print(payload['temp'])
    append_to_csv('example.csv', [str(payload['temp']),str(payload['humid']),str(payload['date'])])
    return payload

# Create an MQTT client
client = mqtt.Client()

# Set the callback function for when a message is received
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, port)

# Subscribe to the specified topic
client.subscribe(topic)

# Loop to listen for messages
client.loop_forever()
