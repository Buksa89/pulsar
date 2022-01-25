from pulsar import Function, schema
import requests

class Foo(schema.Record):
    time_id = schema.Long()
    value = schema.Integer()

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

class sql_api(Function):

    def process(self, input, context):
        input = schema.AvroSchema(Foo).decode(input)

        headers = {'X-Presto-User': 'test-user'}
        data = f'select * from pulsar."public/default".apiin where value={input.value}'
        response = requests.post('http://localhost:8081/v1/statement', headers=headers, data=data)
        
        loops = 0

        while 'data' not in response.json().keys():
            loops+=1
            if 'nextUri' in response.json().keys():
                response = requests.get(response.json()['nextUri'])
            else:
                number_of_rows = 0
                break
        else:
            number_of_rows = len(response.json()['data'])
            
        output = Output()
        output.setValue(input.value)
        if number_of_rows > 0:
            output.set_already_exist(True)
        else:
            output.set_already_exist(False)

        # logger = context.get_logger()
        # logger.warn(loops)
        # logger.warn(output.getValue())
        # logger.warn(output.get_already_exist())
        # logger.warn('-----------------------------')

        
        return schema.AvroSchema(Output).encode(output)
        # return schema.AvroSchema(Foo).encode(Foo(input, context))

#create bin/pulsar-admin functions create --py ~/apache-pulsar-2.9.1/testy/17_sql_api/my_function.py --classname my_function.sql_api --inputs persistent://public/default/apiin --output persistent://public/default/apiouts   
#update bin/pulsar-admin functions update --py ~/apache-pulsar-2.9.1/testy/17_sql_api/my_function.py --classname my_function.sql_api --inputs persistent://public/default/apiin --output persistent://public/default/apiouts   
