import json
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision

INFLUX_URL = "http://localhost:8086"
TOKEN = "Oo48CouBMoAxKPz_Gh1U79JicXWQzv5RMaAGg1Xv8VIKrrzD5lQKWsrjb7MmEZL7PwOQMd-BWGPxRXSAmZ6Ksg=="
ORG = "energy-org"
BUCKET = "energy-bucket"

client_influx = InfluxDBClient(url=INFLUX_URL, token=TOKEN, org=ORG)
write_api = client_influx.write_api()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    point = Point("energy") \
        .tag("device_id", data["device_id"]) \
        .field("voltage", float(data["voltage"])) \
        .field("current", float(data["current"])) \
        .field("power", float(data["power"])) \
        .field("energy", float(data["energy"])) \
        .field("power_factor", float(data["power_factor"])) \
        .field("frequency", float(data["frequency"])) \
        .time(None, WritePrecision.NS)

    write_api.write(bucket=BUCKET, org=ORG, record=point)

    print("Stored:", data)

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("energy/data")

client.loop_forever()
