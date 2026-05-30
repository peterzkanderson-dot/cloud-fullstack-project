import json
import time
import random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    data = {
        "device_id": "meter-001",
        "voltage": round(random.uniform(220, 240), 2),
        "current": round(random.uniform(1, 10), 2),
        "power": round(random.uniform(200, 2000), 2),
        "energy": round(random.uniform(10, 100), 2),
        "power_factor": round(random.uniform(0.8, 1.0), 2),
        "frequency": 50.0
    }

    client.publish("energy/data", json.dumps(data))
    print("Sent:", data)

    time.sleep(2)
