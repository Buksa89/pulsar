from pulsar import Function

class RoutingFunction(Function):
    def __init__(self):
        self.fruits_topic = "persistent://public/default/fruits"
        self.vegetables_topic = "persistent://public/default/vegetables"

    @staticmethod
    def is_fruit(item):
        return item in ["apple", "orange", "pear", "other fruits..."]

    @staticmethod
    def is_vegetable(item):
        return item in ["carrot", "lettuce", "radish", "other vegetables..."]

    def process(self, item, context):
        if self.is_fruit(item):
            context.publish(self.fruits_topic, item)
        elif self.is_vegetable(item):
            context.publish(self.vegetables_topic, item)
        else:
            warning = "The item {0} is neither a fruit nor a vegetable".format(item)
            context.get_logger().warn(warning)

# bin/pulsar-admin functions localrun   --py ~/apache-pulsar-2.9.1/testy/06_grocery/my_function.py   --classname my_function.RoutingFunction   --tenant public   --namespace default   --name grocery   --inputs persistent://public/default/basket-items