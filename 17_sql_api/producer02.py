from pulsar import Client, schema
from time import time

class Output(schema.Record):
    value = schema.Integer()
    already_exist = schema.Boolean()

    def get_already_exist(cls):
        return cls.already_exist
        
    def set_already_exist(cls, already_exist):
        cls.already_exist = already_exist

    def getValue(cls):
        return cls.value

    def setValue(cls, value):
        cls.value = value

client = Client('pulsar://localhost:6650')
producer = client.create_producer('persistent://public/default/apiouts',schema=schema.AvroSchema(Output))

foo = Output()
foo.setValue(46)
foo.set_already_exist(True)

producer.send(foo)

producer.close()
client.close()