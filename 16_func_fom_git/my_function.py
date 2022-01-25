from pulsar import Function
import datetime
#from time import sleep
    
class MyContextStore(Function):
    def __init__(self):
        pass
    
    def process(self, input, context):
        logger=context.get_logger()
        startTime = datetime.datetime.now()
        functionName = context.get_function_name()
        
        logger.info(f'Function: {functionName} started')
        logger.info(f'Function: {functionName} exexuting stream storage stress test now...')    
        for x in range(10000):
            logger.info('-- Store Context variable Loop: %s --' % x)
            strx=str(x)
            context.put_state('key'+strx, 'value1')
            foo=context.get_state('key'+strx)
            logger.info('-- The value for ''key%s'' is: %s (Loop: %s) --' % (strx, foo, x))
        logger.info(f'Function: {functionName} Stress test end...')    
        logger.info(f'Function: {functionName} ended')
        return foo



# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/16_func_fom_git/my_function.py   --classname my_function.MyContextStore   --tenant public   --namespace default   --name from_git   --inputs persistent://public/default/input    --output persistent://public/default/output