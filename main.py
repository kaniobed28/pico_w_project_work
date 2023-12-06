from lcd1602 import LCD1602
from dht import DHT11
from machine import I2C,Pin,ADC
from utime import sleep
import network
import time
import json
import utime



from umqtt.simple import MQTTClient


def send_mqtt_message(message,broker):
    # Replace these values with your MQTT broker information
    mqtt_broker = broker
    mqtt_port = 1883
    mqtt_user = "your_username"
    mqtt_password = "your_password"
    mqtt_topic = "day_temp_humd"

    # Generate a unique client ID based on the device's unique ID
    client_id = "pico_"

    try:
        # Connect to the MQTT broker
        client = MQTTClient(client_id, mqtt_broker, port=mqtt_port)
        client.connect()

        # Publish the message to the specified topic
        client.publish(mqtt_topic, message)

        # Disconnect from the broker
        client.disconnect()

        print("MQTT message sent successfully.")
    except Exception as e:
        print("Error sending MQTT message:", e)



def netWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    wlan.connect("kaniobed28","33333333")
    while not wlan.isconnected():
        print("connecting...")
        time.sleep(1)
        
    print("connected")
netWifi()


i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
mydht = DHT11(Pin(18))

while True:
    
    mydht.measure()
    temp=mydht.temperature()

    humid=mydht.humidity()
    d.clear()
    d.setCursor(0,0)
    
    d.print("Temp: %.1f C"%temp)
    #print("Temp: %.1f"%temp)
    d.setCursor(0,1)
    d.print("Humid: %.1f"%humid)
    #print("Humid: %.1f"%humid)
    

    current_time = utime.localtime(utime.time())
    formatted_time = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(*current_time)

    
    data = {"temp":temp,"humid":humid,"date":formatted_time}
    sleep(1)
    send_mqtt_message(f'{data}',"broker.hivemq.com")


    
