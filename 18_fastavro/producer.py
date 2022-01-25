from pulsar import Client, schema
from time import time
from Foo import Foo
from random import randint

client = Client('pulsar://localhost:6650')
producer = client.create_producer('persistent://public/default/inputFixed',schema=schema.AvroSchema(Foo))

value = randint(11,14)

foo = Foo()
foo.setValue(value)
foo.setID(int(time()))

producer.send(foo)

producer.close()
client.close()