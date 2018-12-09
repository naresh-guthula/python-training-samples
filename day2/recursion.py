import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(5)

print(sys.getrecursionlimit())


def fact(n):
    # print('{} ({})'.format())
    if n:
        return n * fact(n - 1)
    else:
        return 1


print()
print(fact(3))
