# Author: Aljawharah Almuhana

import time
import logging
from confluent_kafka import Consumer, KafkaException
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_file(file_path, content):
    with open(file_path, 'wb') as file:
        file.write(content)

def main():
    consumer_conf = {
        'bootstrap.servers': config.KAFKA_CONSUMER_CONFIG['bootstrap.servers'],
        'group.id': config.KAFKA_CONSUMER_CONFIG['group.id'],
        'auto.offset.reset': config.KAFKA_CONSUMER_CONFIG['auto.offset.reset'],
        'max.partition.fetch.bytes': config.KAFKA_CONSUMER_CONFIG['max.partition.fetch.bytes']
    }

    consumer = Consumer(consumer_conf)
    consumer.subscribe([config.TOPIC_NAME])

    try:
        while True:
            message = consumer.poll(1.0)
            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaException._PARTITION_EOF:
                    # End of partition event
                    logger.info('End of partition reached {0}/{1}'.format(message.topic(), message.partition()))
                else:
                    logger.error(f"Error: {message.error()}")
                continue

            file_content = message.value()
            file_name = message.key().decode('utf-8')
            save_file(file_name, file_content)
            logger.info(f'File saved as: {file_name}')

            consumer.commit(message)

    except KeyboardInterrupt:
        logger.info("Interrupted by user")

    finally:
        consumer.close()

if __name__ == '__main__':
    main()
