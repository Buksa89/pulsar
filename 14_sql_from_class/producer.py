from pulsar import Client, schema
from Foo import Foo
from time import time

client = Client('pulsar://localhost:6650')
producer = client.create_producer('persistent://public/default/sqlfc',schema=schema.AvroSchema(Foo))


for i in range(10):
    foo = Foo()
    foo.setField1(i)
    foo.setField2("foo" + str(i))
    foo.setField3(int(time()))

producer.send(foo)


producer.close()
client.close()
    



