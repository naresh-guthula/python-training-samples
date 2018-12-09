import re
from fileinput import filelineno, filename, input  # cherry picking, you can use alias, import as ____


def grep_me(pattern, *args):
    for line in input(args):
        if re.search(pattern, line, re.I):
            print('{}:{}:{}'.format(filename(), filelineno(), line), end='')  # variable interpolation-> string formatting


grep_me('root', 'password.txt', 'password1.txt')
