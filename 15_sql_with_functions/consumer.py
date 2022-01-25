import pulsar
import random 
import string
from Foo import Foo
from pulsar import schema

name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(topic = 'persistent://public/default/sqlout2', subscription_name = name, schema=schema.AvroSchema(Foo))

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