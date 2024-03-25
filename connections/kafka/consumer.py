import sys

from confluent_kafka import Consumer, KafkaError

conf = {'bootstrap.servers': '127.0.0.1:29092',
        'group.id': 'eyal_group3',
        'session.timeout.ms': 6000,
        'auto.offset.reset': 'earliest'
        }

consumer = Consumer(conf)
consumer.subscribe(['eyal_topic'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            print(f"msg is none for this partition ")
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(msg.partition())
                continue
            else:
                print(msg.error())
                break
        else:
            print(f"this is the message {msg.value().decode()}", msg.partition())

except Exception as e:
    print(e)
    print(type(e).__name__)
    print(sys.exc_info())

finally:
    consumer.close()


