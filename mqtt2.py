import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

rc, mid = client.publish("mqtt/shingu/test", "Hello MQTT!!")
print(str(rc))