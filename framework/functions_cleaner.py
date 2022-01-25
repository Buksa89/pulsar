import os, sys
import subprocess

pulsar_admin_path = '~/apache-pulsar-2.9.1/bin/pulsar-admin'
cmd_list = pulsar_admin_path + ' functions list'

result = os.popen(cmd_list).read()
result = result.split('\n')
functions = list(map(lambda x: x[1:-1], result))[:-1]
cmd_del = pulsar_admin_path + ' functions delete --name '
for num, function_ in enumerate(functions):
    print(f'{num+1}/{len(functions)}\tREMOVING: {function_}')
    result = os.popen(cmd_del+function_).read()

print('JOB DONE!')