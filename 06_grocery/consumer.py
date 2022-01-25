import pulsar
import random
import string
name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('persistent://public/default/fruits', name)

while True:
    msg = consumer.receive()
    try:
        print(f"Fruit '{msg.data()}'")
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()