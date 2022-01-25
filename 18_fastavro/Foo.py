from pulsar import schema

class Foo(schema.Record):
    time_id = schema.Long()
    value = schema.Integer()

    def getID(cls):
        return cls.time_id
        
    def setID(cls, time_id):
        cls.time_id = time_id

    def getValue(cls):
        return cls.value

    def setValue(cls, value):
        cls.value = value