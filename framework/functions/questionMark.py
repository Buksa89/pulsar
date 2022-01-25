from pulsar import Function

class questionMark(Function):

    def process(self, item, context):
        return '?'+item