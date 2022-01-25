from pulsar import Client, schema

class Foo():
    def __init__(self) -> None:
        self.__field1 = 1   #int
        self.__field2 = ''  #str
        self.__field3 = ''  #long

    def getField1(self):
        return self.__field1
        
    def setField1(self, field1):
        self.__field1 = field1

    def getField2(self):
        return self.__field2

    def setField2(self, field2):
        self.__field2 = field2

    def getField3(self):
        return self.__field3

    def setField2(self, field3):
        self.__field3 = field3

def main (self, *args, **kwargs):
    client = Client('pulsar://localhost:6650')
    producer = client.create_producer('persistent://public/default/input',schema=schema.AvroSchema(Foo))

#     public static void main(String[] args) throws Exception {
#         PulsarClient pulsarClient = PulsarClient.builder().serviceUrl("pulsar://localhost:6650").build();
#         Producer<Foo> producer = pulsarClient.newProducer(AvroSchema.of(Foo.class)).topic("test_topic").create();

#         for (int i = 0; i < 1000; i++) {
#             Foo foo = new Foo();
#             foo.setField1(i);
#             foo.setField2("foo" + i);
#             foo.setField3(System.currentTimeMillis());
#             producer.newMessage().value(foo).send();
#         }
#         producer.close();
#         pulsarClient.close();
#     }
# }




schema.Stri



client = Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/input')

input = '8'
producer.send(input.encode('utf-8'))

client.close()


