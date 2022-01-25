from pulsar import Function

class myFunction(Function):

    def process(self, input, context):
        context.record_metric('hit-count', 1)

        if input == "11":
            context.record_metric('elevens-count', 1)
        #???? Jak dostac sie do metryk????
# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/09_metrics/my_function.py   --classname my_function.myFunction   --tenant public   --namespace default   --name metrics   --inputs persistent://public/default/input    --output persistent://public/default/output