from pickle import FALSE
import pulsar

from pulsar import schema
from pulsar import Client


class Example(schema.Record):
    a = schema.String()
    b = schema.Integer()
    c = schema.Boolean()

client = Client('pulsar://localhost:6650')
# producer = client.create_producer('persistent://public/default/output')
# producer = client.create_producer('output',schema=schema.StringSchema())
producer = client.create_producer('sql',schema=schema.AvroSchema(Example))

producer.send(Example(a="Sandbox", b=1, C=False))
