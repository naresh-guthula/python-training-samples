class Product:
    def __init__(self, p_id):
        self.p_id = p_id

    def __str__(self):
        return '{} #id:{}'.format(self.__class__.__name__, self.p_id)

    __repr__ = __str__


class Cart:
    def __init__(self):
        self.cart = list()

    def add(self, p):
        pass
        self.cart.append(p)

    def __str__(self):
        return '{} contains = {}'.format(self.__class__.__name__, self.cart)


if __name__ == '__main__':
    c = Cart()
    c.add(Product(123))
    c.add(Product(234))
    print(c)
