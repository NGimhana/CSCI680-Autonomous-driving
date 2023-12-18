# Author: Aljawharah Almuhana

# this is configuration settings for Kafka Producer
KAFKA_PRODUCER_CONFIG = {
    'bootstrap.servers': '127.0.0.1:9092',
    'message.max.bytes': '30000000',  
    # 127.0.0.1 used becaues I test in my local machine 
}

# this is  configuration settings for Kafka Consumer
KAFKA_CONSUMER_CONFIG = {
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest',
    'max.partition.fetch.bytes': '30000000',  
}

TOPIC_NAME = 'OTA'

#this is where we can change the config like bytes, topic name etc. 
