def get_integers():
    i = 1
    while True:
        yield i
        i += 1


squares = (i ** 2 for i in get_integers())


def take_n(count, squares):
    for element in range(count):
        yield next(squares)


if __name__ == '__main__':
    n = take_n(5, squares)
    for square in n:
        print(n)
