"""
lambda functions
lambda arg1, arg2.....: expression
"""

power = lambda x, n: x ** n
print(power)
print(pow(2, 3))


def accept_lambda(fun):
    print(fun(2, 3))

accept_lambda(lambda x, n: x ** n)