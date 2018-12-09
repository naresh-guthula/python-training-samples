# python -m pip install requests
import requests
from pprint import pprint as pp


def get_tasks():
    url = 'http://127.0.0.1:5000/todo/tasks'
    return pp(requests.get(url).json())


def create_task():
    url = 'http://127.0.0.1:5000/todo/tasks'
    payload = dict(title='last task')
    res = requests.post(url, json=payload)
    print(res.status_code)
    with open('tasks.json', 'w') as fw:
        print(res.content.decode('ascii'), file=fw)


if __name__ == '__main__':
    print(get_tasks())
    print(create_task())
