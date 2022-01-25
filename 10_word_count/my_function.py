from pulsar import Function

class myFunction(Function):

    def process(self, input, context):
        # words = input.split()
        # for word in words:
        #     context.incr_counter("words", 1)
        # return str(context.get_counter("words"))

        return input
        



# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/10_word_count/my_function.py   --classname my_function.myFunction   --tenant public   --namespace default   --name word_count   --inputs persistent://public/default/input    --output persistent://public/default/output
# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/10_word_count/my_function.py   --classname my_function.myFunction   --tenant public   --namespace default   --name word_count --state-storage-url localhost:4182   --inputs persistent://public/default/input    --output persistent://public/default/output