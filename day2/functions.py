# def demo():
#     print('null arguments')

# print(demo)
# print()
# print(type(demo))

# def demo(a, b):
#     print(a+b)

# demo() # fail

"""positional argument aka fixed"""
# def power(x, n=0):
#     return x ** n
#
# print(power(4, 2))

"""variable length"""
# def varArgsFunction(*args):
#     print(args)
#
# varArgsFunction(1,2,3)
# items = [1,2,3]
# print(varArgsFunction(items))
# print(varArgsFunction(*items))
#




def compute(a, b, c):
    print(a +b +c)

items = [11, 22, 33]
compute(items[0], items[1], items[2])
compute(*items)
items = [11, 22, 33, 44]
compute(*items[:3])




