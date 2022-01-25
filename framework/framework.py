import os
import subprocess

from sqlalchemy import func
# Deklaracja ścieżek
pulsar_admin_path = '~/apache-pulsar-2.9.1/bin/pulsar-admin'
functions_path = '~/apache-pulsar-2.9.1/testy/framework/functions'

# Deklaracja topików wejściowych i wyjściowych
input_tenant = 'public'
input_namespace = 'default'
input_topic = 'framework_input'

output_tenant = 'public'
output_namespace = 'default'
output_topic = 'framework_output'

scenario_tenant = 'public'
scenario_namespace = 'default'

# Nazwa scenariusza
scenario_name = 'first_run'

# Kolejne kroki
steps = ['exclamationMark', 'questionMark', 'questionMark']




# Tego nie zmieniać
input_topic = f'persistent://{input_tenant}/{input_namespace}/{input_topic}'
output_topic = f'persistent://{input_tenant}/{output_namespace}/{output_topic}'
tour = []

# Utworzenie paramterów:

for num, function_ in enumerate(steps):
    parameters = {}
    parameters['py'] = os.path.join(functions_path, function_+'.py')
    parameters['classname'] = f'{function_}.{function_}'

    parameters['name'] = f'{scenario_name}_{str(num).zfill(3)}_{function_}'
    
    next_name = f'{scenario_name}_{str(num+1).zfill(3)}_{function_}'
    if num == 0:
        parameters['inputs'] = input_topic
    else:
        last_name = tour[num-1]['name']
        parameters['inputs'] = f'persistent://{scenario_tenant}/{scenario_namespace}/{last_name}'

    if num == len(steps)-1:
        parameters['output'] = output_topic
    else:
        parameters['output'] =  f'persistent://{scenario_tenant}/{scenario_namespace}/{parameters["name"]}'
    
    tour.append(parameters)

# Wyświetlenie parametrów:
# for step in tour:
#     for k, v in step.items():
#         print(f'\t\t{k}: \t{v}')
#     print('----')

for num, step in enumerate(tour):
    print(f'{num+1}/{len(tour)}\tCREATING: {step["name"]}')
    command_ = f'{pulsar_admin_path} functions create'
    for k, v in step.items():
        command_ += f' --{k} {v}'
    os.popen(command_).read()
print('JOB DONE!')

# bin/pulsar-admin functions create   --py ~/apache-pulsar-2.9.1/testy/03_exclamation_mark/my_function.py   --classname my_function.excMark   --tenant public   --namespace default   --name excMark   --inputs persistent://public/default/inputexcmark    --output persistent://public/default/outputexcmark