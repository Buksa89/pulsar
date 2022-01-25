from pulsar import Function

class exclamationMark(Function):

    def process(self, item, context):
        return '!'+item