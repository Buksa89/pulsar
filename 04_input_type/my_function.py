from pulsar import Function
from pulsar import schema

class condition(Function):

    def process(self, item, context):
        if item == 'input':
            return schema.Boolean.encode(True)
        else: 
            return schema.Boolean.encode(False)

# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/04_input_type/my_function.py   --classname my_function.condition   --tenant public   --namespace default   --name condition   --inputs persistent://public/default/inputcondition    --output persistent://public/default/outputcondition