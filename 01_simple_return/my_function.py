from pulsar import Function

class myFunction01(Function):

    def process(self, input, context):
        return 'return'

# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/01_simple_return/my_function.py   --classname my_function.myFunction01   --tenant public   --namespace default   --name simple_return   --inputs persistent://public/default/input1    --output persistent://public/default/output1