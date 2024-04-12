from data_storage.database import Database
from data_consumer.kafka import Kafka
import sys
database=Database()
import json


def add_data(value):
    
        print(value)
    
consumer=Kafka(["0.0.0.0:9093","0.0.0.0:9092","0.0.0.0:9094"])


consumer.basic_consume_loop(topics=["products",],callback=add_data)
