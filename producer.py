from kafka import KafkaProducer

kafka_topic = "shop_testing"

def run_producer(message):
    producer = KafkaProducer(bootstrap_servers="192.168.124.193:9092")
    
    print("sending data to kafka_topic....")
    
    data = ",".join(message)
    
    producer.send(topic=kafka_topic, value=data.encode('utf-8'))
    
    print("message successfully sent to kafka_topic")
        
    producer.flush()

    producer.close()


run_producer(["aaronpinto1@gmail.com", "Banku and Stew", "12/03/24"])
