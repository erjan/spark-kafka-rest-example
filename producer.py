from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = 'sending'

for e in range(1000):
    # data = {'number' : e}
    producer.send(topic, value=e)
    sleep(1)