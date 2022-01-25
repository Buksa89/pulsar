from pulsar import Function

class LoggingFunction(Function):
    def __init__(self):
        pass
    def process(self, input, context):
        logger = context.get_logger()
        msg_id = context.get_message_id()
        if 'danger' in input:
          logger.warn("A warning was received in message {0}".format(context.get_message_id()))
        else:
          logger.info("Message {0} received\nContent: {1}".format(msg_id, input))

# Ponizsze tez dziala
# def process(self, input, context):
# context.get_logger().info(input + '-logo')
# return input + '!'

# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/07_logs_save/my_function.py   --classname my_function.LoggingFunction  --tenant public   --namespace default   --name LoggingFunction   --inputs persistent://public/default/input    --output persistent://public/default/output