from pulsar import Function, schema
import requests
import fastavro
import io

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


class outputFixed(Function):

    def process(self, input, context):
        buffer = io.BytesIO(input)
        input = fastavro.schemaless_reader(buffer, Foo.schema())
        # logger = context.get_logger()
        # logger.warn(input)

        headers = {'X-Presto-User': 'test-user'}
        data = f'select * from pulsar."public/default".inputFixed where value={input["value"]}'
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
            
        output = {'value':input['value'], 'already_exist':False}
        if number_of_rows > 0:
            output['already_exist'] = True

        logger = context.get_logger()
        logger.warn(output)

        outbuffer = io.BytesIO()
        fastavro.schemaless_writer(outbuffer, Output.schema(), output)

        # output_topic = context.instance_config.function_details.sink.topic
        # context.publish(output_topic, outbuffer.getvalue())

        return outbuffer.getvalue()

# # bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/18_output_fix/my_function.py   --classname my_function.outputFixed   --tenant public   --namespace default   --name outputFixed   --inputs persistent://public/default/inputFixed  --output persistent://public/default/outputFixed
# # bin/pulsar-admin functions update   --py ~/apache-pulsar-2.9.1/testy/18_output_fix/my_function.py   --classname my_function.outputFixed   --tenant public   --namespace default   --name outputFixed   --inputs persistent://public/default/inputFixed  --output persistent://public/default/outputFixed