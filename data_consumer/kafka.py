from confluent_kafka import Consumer,KafkaError,KafkaException
from data_storage.database import Database
import sys
import json


class Kafka:

    def __init__(self,hosts:list,group_id:str="foo") -> None:
        conf = {'bootstrap.servers': ",".join(hosts),'group.id': group_id,'auto.offset.reset': 'smallest'}
        self.consumer = Consumer(conf)
        self.database=Database()
        self.running = True

    def basic_consume_loop(self, topics, callback):
        try:
            self.consumer.subscribe(topics)

            while self.running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                        (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    callback(json.loads(msg.value().decode()))
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()

    def shutdown(self):
        running = False


        
