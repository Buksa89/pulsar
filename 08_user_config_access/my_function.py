from pulsar import Function

class myFunction(Function):
    def process(self, input, context):
        logger = context.get_logger()
        wotd = context.get_user_config_value('word-of-the-day')
        if wotd is None:
            logger.warn('No word of the day provided')
        else:
            logger.info("The word of the day is {0}".format(wotd))
            
# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/08_user_config_access/my_function.py   --classname my_function.myFunction   --tenant public   --namespace default   --name user_config_access   --inputs persistent://public/default/input    --output persistent://public/default/output
# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/08_user_config_access/my_function.py   --classname my_function.myFunction  --user-config '{"word-of-the-day":"verdure"}'   --tenant public   --namespace default   --name user_config_access   --inputs persistent://public/default/input    --output persistent://public/default/output