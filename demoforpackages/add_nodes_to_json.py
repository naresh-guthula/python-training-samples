from pprint import pprint as pp

content = load(open('tasks.json'))

for key, list_of_task in content.items():
    for task in list_of_task:
        task.update(dict(owner='ravi', priority=5))

with open('updated.json', 'w') as fw:
    dump(content, fw, indent=4)