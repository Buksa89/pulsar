import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/basket-items')

product = 'carrot'
producer.send(product.encode('utf-8'))


client.close()