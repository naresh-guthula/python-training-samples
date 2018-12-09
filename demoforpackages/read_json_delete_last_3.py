from json import load, dump
from pprint import pprint as pp

content = load(open('tasks.json'))

content['tasks'] = content['tasks'][:3]

dump(content, open('modified.json', 'w'), indent=4)
