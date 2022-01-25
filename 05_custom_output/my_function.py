from pulsar import Function

class customOutput(Function):

    def process(self, item, context):
        output = 'persistent://public/default/customoutput'
        context.publish(output, item)
# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/05_custom_output/my_function.py   --classname my_function.customOutput   --tenant public   --namespace default   --name customOutput   --inputs persistent://public/default/custominput  --output persistent://public/default/customoutput