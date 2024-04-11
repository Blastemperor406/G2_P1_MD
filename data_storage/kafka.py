from confluent_kafka import Producer
import socket
import json



class Kafka:

    def __init__(self,hosts:list,topic:str="products",clientID:str=socket.gethostname()):

# conf = {'bootstrap.servers': '172.25.0.6:9093,172.25.0.3:9092,172.25.0.4:9094','client.id': socket.gethostname()}
        self.topic=topic
        conf = {'bootstrap.servers': ','.join(hosts),'client.id': clientID}
        self.producer = Producer(conf)
        print("Producer configured")
    def acked(self,err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    def insert_products(self,msg:dict):
        
            self.producer.produce(self.topic, key=msg["Name"], value=json.dumps(msg), callback=self.acked)
            self.producer.poll()

if __name__=="__main__":
    producer=Kafka(["0.0.0.0:9093","0.0.0.0:9092","0.0.0.0:9094"])

    for i in range(100):
        producer.insert_product({"key":str(i),"value":[i,"yo"]})
