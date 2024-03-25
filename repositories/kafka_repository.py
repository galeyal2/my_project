import sys
from typing import Optional

from connections.kafka.producer import OpenKafkaConn
from utils.my_logger import eyal_logger

kafka_conn = OpenKafkaConn()
producer = kafka_conn.producer


class KafkaRepository:
    def __init__(self, topic=None, config=None):
        self.kafka_conn = OpenKafkaConn(topic, config)
        self.producer = self.kafka_conn.producer

    def send_msg(self, msg: dict, key: Optional[int] = None):
        try:
            self.producer.producer.produce(topic=self.producer.topic, value=str(msg).encode('utf-8'), partition=key)
            self.producer.producer.flush()
            eyal_logger.info("Message sent")
        except Exception as e:
            eyal_logger.error(e)
            eyal_logger.error(sys.exc_info())