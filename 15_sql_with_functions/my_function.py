from pulsar import Function, schema

class Foo(schema.Record):
    field1 = schema.Integer()
    field2 = schema.String()
    field3 = schema.Long()

class sql_with_functions(Function):

    def process(self, input, context):
        #print(str(args)) #(b'\x02\x12\x02\x08foo9\x02\xb0\xcf\xd6\x9e\x0c', <contextimpl.ContextImpl object at 0x7fcf242468e0>)
        
        input = schema.AvroSchema(Foo).decode(input)


        logger = context.get_logger()
        logger.warn("inpt: {0}".format(input))

        return schema.AvroSchema(Foo).encode(Foo(input, context))


# from pulsar import Function, schema

# class Foo(schema.Record):
#     field1 = schema.Integer()
#     field2 = schema.String()
#     field3 = schema.Long()

# class Schema:
#     schema = None

#     def __init__(self, *args):
#         print("args2", str(args)) # args: (<pulsar.schema.schema_avro.AvroSchema object at 0x7fe0f505f6d0>,)
#         self.schema = args[0]

#     def __call__(self, f):
#         def wrapped(*args): #args wygladaja tak: (<my_function.sql_with_functions object at 0x7fba450516a0>, b'\x02\x12\x02\x08foo9\x02\xa0\x90\xd6\x9e\x0c', <contextimpl.ContextImpl object at 0x7fba44f949d0>)
#             args = list(args)
#             args[1] = self.schema.decode(args[1])
#             return self.schema.encode(f(*tuple(args)))
#         return wrapped

# class sql_with_functions(Function):
#     def __init__(self):
#         pass

#     @Schema(schema.AvroSchema(Foo))
#     def process(self, input, context):
#         logger = context.get_logger()
#         logger.warn("Message: {0}".format(input))
#         logger.warn("Name: {0}".format(input.field1))

#         return input



#create bin/pulsar-admin functions create --py ~/apache-pulsar-2.9.1/testy/15_sql_with_functions/my_function.py --classname my_function.sql_with_functions --inputs persistent://public/default/sqlin --output persistent://public/default/sqlout2
#update bin/pulsar-admin functions update --py ~/apache-pulsar-2.9.1/testy/15_sql_with_functions/my_function.py --classname my_function.sql_with_functions --inputs persistent://public/default/sqlin --output persistent://public/default/sqlout2

