from pulsar import Function

class excMark(Function):

    def process(self, item, context):
        return '!'+item

# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/03_exclamation_mark/my_function.py   --classname my_function.excMark   --tenant public   --namespace default   --name excMark   --inputs persistent://public/default/inputexcmark    --output persistent://public/default/outputexcmark