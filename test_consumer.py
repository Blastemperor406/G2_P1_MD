from data_storage.database import Database
from data_consumer.kafka import Kafka
import sys
database=Database()
import json
import g2_filter


def add_data(value):
    try:
        print(value)
        database.insert_products(value)
    except Exception as e:
        print(e)

consumer=Kafka(["kafka1:9092","kafka2:9093","kafka3:9094"])

consumer.basic_consume_loop(topics=["products",], callback=lambda value: g2_filter.g2_filter(d=value, function_call=add_data))
