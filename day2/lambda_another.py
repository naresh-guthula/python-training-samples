import re

pattern = 'bash$'


def my_filter(func, seq):
    return [item for item in seq if func(item)]


f = filter(lambda line: re.search(pattern, line, re.I), open('password.txt'))
f = my_filter(lambda line: re.search(pattern, line, re.I), open('password.txt'))

for matched_line in f:
    print(matched_line, end='')
