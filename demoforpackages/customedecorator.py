def argument_logger(func):
    def logger_handler(*args):
        value = func(*args)
        print('called {}{} and return {}'.format(func.__name__, args, value))
        return value

    return logger_handler


@argument_logger
def compute(a, b):
    return dict(result=a + b)


print(compute)
print(compute(33, 44))
print()
print(compute('perter', 'pan'))
