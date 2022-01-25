import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/input1')

input = 'input'
producer.send((input).encode('utf-8'))

client.close()