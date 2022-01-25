from pulsar import Function

class avg(Function):
 
    def process(self, input, context):
        context.incr_counter("number_of_values", 1)
        context.incr_counter("total_of_values", int(input))
        context.put_state("avg", str(context.get_counter('total_of_values')/context.get_counter('number_of_values')))

        return context.get_state("avg")

#create bin/pulsar-admin functions create --py ~/apache-pulsar-2.9.1/testy/12_avg/my_function.py --classname my_function.avg --inputs persistent://public/default/input --output persistent://public/default/output    
#update bin/pulsar-admin functions update --py ~/apache-pulsar-2.9.1/testy/12_avg/my_function.py --classname my_function.avg --inputs persistent://public/default/input --output persistent://public/default/output    
