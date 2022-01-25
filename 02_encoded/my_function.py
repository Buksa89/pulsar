from pulsar import Function

class myFunction(Function):

    def process(self, item, context):
        return item

# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/02_encoded/my_function.py   --classname function.myFunction   --tenant public   --namespace default   --name encoded   --inputs persistent://public/default/input    --output persistent://public/default/output