import pulsar
import random 
import string
from pulsar import schema

class Output(schema.Record):
    value = schema.Integer()
    already_exist = schema.Boolean()

name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(topic = 'persistent://public/default/outputFixed2', subscription_name = name, schema=schema.AvroSchema(Output))

while True:
    try:
        msg = consumer.receive()
        print(msg.value())
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()