import paho.mqtt.client as mqtt

# MQTT 브로커에 연결되었을 때 특정 토빅(여기서는 mqtt/shingu/test 토빅)을 구축한다.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))
    topic = "mqtt/shingu/test"
    client.subscribe(topic)

# 토픽으로 게시가 발생했을 때 브로커에서 클라이언트로 메시지를 전송한 것을 받을
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()

#연결 및 메시지 수진 콜백 함수를 등록
client.on_connect = on_connect
client.on_message = on_message

#모스키토 테스트 MQTT 브로커에 연결
client.connect("test.mosquitto.org", 1883, 60)

#메시지 루프 시작
client.loop_forever()