import os
import pprint


class SystemInformation:
    def __init__(self):
        print(self, 'am constructor')

    def __del__(self):
        print(self, 'getting destroyed...')


# if 1 == 1:
#     pass  # dummy code block

if __name__ == '__main__':
    print(__name__)
    s1 = SystemInformation()
    print(s1)
    print()
    print(SystemInformation)
    print(os.__name__)
    print(pprint.__name__)
    print(globals())
