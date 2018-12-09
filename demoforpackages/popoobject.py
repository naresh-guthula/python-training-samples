class Person:
    def __init__(self):
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    p = Person()
    print(p.name)
    p.name = 'larry wall'
    print(p.name)
