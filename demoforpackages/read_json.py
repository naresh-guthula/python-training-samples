from json import load
from pprint import pprint as pp

content = load(open('tasks.json'))

for key, list_of_task in content:
    print(key)

    for task in list_of_task:
        for caption, value in task.items():
            print('\t', caption, ':', value)

        print()
