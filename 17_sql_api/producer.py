from pulsar import Client, schema
from time import time
from Foo import Foo
from random import randint

client = Client('pulsar://localhost:6650')
producer = client.create_producer('persistent://public/default/apiin',schema=schema.AvroSchema(Foo))

value = randint(11,14)

foo = Foo()
foo.setValue(value)
foo.setID(int(time()))

producer.send(foo)

producer.close()
client.close()


# import requests

# import requests

# headers = {
#     'X-Presto-User': 'test-user',
# }

# data = 'select * from pulsar."public/default".sqlin'
# # data = 'show catalogs'
# response = requests.post('http://localhost:8081/v1/statement', headers=headers, data=data)
# while 'data' not in response.json().keys():
#     print ('--', response.json()['nextUri'])
#     response = requests.get(response.json()['nextUri'])
# # while 'nextUri' in response.json().keys():
# #     print ('--', response.json()['nextUri'])
# #     response = requests.get(response.json()['nextUri'])
# # response = requests.get(response.json()['nextUri'])
# # response = requests.get(response.json()['nextUri'])
# # response = requests.get(response.json()['nextUri'])

# # for k, v in response.json().items():
# #     print(k)
# #     print('--------')


# for i in response.json()['data']:
#     print(i)
#     print('--------')

# # print(response.json())