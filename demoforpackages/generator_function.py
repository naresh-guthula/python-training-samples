def demo():
    # print('before1')
    # return 11
    # print('after 1')
    #
    # print('before2')
    # return 11
    # print('after 2')
    #
    # print('before3')
    # return 11
    # print('after 3')

    print('before1')
    yield 11
    print('after 1')

    print('before2')
    yield 11
    print('after 2')

    print('before3')
    yield 11
    print('after 3')


g = demo()
print(next(g))
print('-' * 22)
print(next(g))
