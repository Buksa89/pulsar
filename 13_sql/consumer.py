import pulsar
import random 
import string

from pulsar import schema

class Example(schema.Record):
    a = schema.String()
    b = schema.Integer()
    c = schema.Boolean()

name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(topic = 'persistent://public/default/sql', subscription_name = name, schema=schema.AvroSchema(Example))

while True:
    msg = consumer.receive()
    try:
        msg = consumer.receive()
        print(msg.value())
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()