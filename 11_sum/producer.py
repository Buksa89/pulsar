import pulsar
 
client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/input')

input = '884'
producer.send(input.encode('utf-8'))

client.close()