from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import sys

sys.path.append("../ml")

from ids_model import detect_attack

consumer = KafkaConsumer(
    'network-logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

es = Elasticsearch("http://localhost:9200")

print("IDS Consumer started...")

for message in consumer:

    log = message.value

    port = log["port"]
    bytes_sent = log["bytes"]

    attack = detect_attack(port, bytes_sent)

    log["attack"] = attack

    if attack:
        print("⚠️ ATTACK DETECTED:", log)
        es.index(index="attack-alerts", document=log)
    else:
        print("Normal traffic:", log)
        es.index(index="network-traffic", document=log)
