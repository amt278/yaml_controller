import yaml

data = {
    'name': 'sam3an',
    'age': 100
 }

with open('write.yml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
