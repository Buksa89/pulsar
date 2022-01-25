from pulsar import Function

class myFunction(Function):

    def process(self, input, context):

        context.incr_counter("sum", 1)
        return f"wykonane, {context.get_counter('sum')}"





# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/11_sum/my_function.py   --classname my_function.myFunction   --tenant public   --namespace default   --name sum   --inputs persistent://public/default/input    --output persistent://public/default/output
