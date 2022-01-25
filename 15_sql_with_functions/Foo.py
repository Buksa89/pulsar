from pulsar import schema

class Foo(schema.Record):
    field1 = schema.Integer()
    field2 = schema.String()
    field3 = schema.Long()

    def getField1(cls):
        return cls.field1
        
    def setField1(cls, field1):
        cls.field1 = field1

    def getField2(cls):
        return cls.field2

    def setField2(cls, field2):
        cls.field2 = field2

    def getField3(cls):
        return cls.field3

    def setField3(cls, field3):
        cls.field3 = field3