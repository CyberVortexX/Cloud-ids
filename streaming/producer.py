from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Traffic generator started...")

while True:

    # randomly simulate attacks
    attack_mode = random.choice([True, False, False, False])

    if attack_mode:
        log = {
            "src_ip": "192.168.1.250",  # attacker IP
            "dst_ip": f"10.0.0.{random.randint(1,255)}",
            "port": random.choice([22,3389]),
            "bytes": random.randint(6000,12000),
            "protocol": "TCP",
            "timestamp": time.time()
        }
    else:
        log = {
            "src_ip": f"192.168.1.{random.randint(1,255)}",
            "dst_ip": f"10.0.0.{random.randint(1,255)}",
            "port": random.choice([80,443]),
            "bytes": random.randint(200,3000),
            "protocol": random.choice(["TCP","UDP"]),
            "timestamp": time.time()
        }

    producer.send("network-logs", log)

    print("Sent:", log)

    time.sleep(2)
