from confluent_kafka import Producer


class OpenKafkaConn():

    def __init__(self, topic=None, config:dict=None):
        self.topic = topic or 'eyal_topic'
        self.config = config or {'bootstrap.servers': 'localhost:29092'}
        self.producer = Producer(self.config)

