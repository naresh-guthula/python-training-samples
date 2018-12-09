n = 10  # global scope


def demo():
    print(n)
    print(globals()['n'])


# update global value
def update_value():
    global n
    n = 'pip'


demo()
print(n)
