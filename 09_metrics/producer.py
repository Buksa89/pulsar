import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/input')

input = 11
producer.send(str(input).encode('utf-8'))

client.close()