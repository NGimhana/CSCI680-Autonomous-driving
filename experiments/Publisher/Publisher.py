# Author: Aljawharah Almuhana

import time
import logging
from confluent_kafka import Producer
import argparse
import config  

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def delivery_report(err, msg):
    if err is not None:
        logger.error(f'Message delivery failed: {err}')
    else:
        logger.info(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')

def publish_file(producer, topic, key, file_path):
    with open(file_path, 'rb') as file:
        value = file.read()
        producer.produce(topic, key=key, value=value, callback=delivery_report)
        producer.poll(0)
    producer.flush()


    

def main(input_file):
    producer_conf = config.KAFKA_PRODUCER_CONFIG
    producer = Producer(producer_conf)


    topic = config.TOPIC_NAME
    key = input_file.split('/')[-1]  

    start_time = time.time()
    publish_file(producer, topic, key, input_file)
    producer.flush()

    end_time = time.time()
    duration = end_time - start_time
    logger.info(f'Time taken to publish: {duration:.2f} seconds')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Args for Kafka Publisher")    
    parser.add_argument("--input_file", type=str, required=True, help="input file path")
    args = parser.parse_args()
    main(args.input_file)
