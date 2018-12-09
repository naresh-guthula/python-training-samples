class Alpha:
    def pprint(self):
        print('pprint from the class Alpha')


class Beta:
    def pprint(self):
        print('pprint from the class Beta')


class Charlie(Beta, Alpha):
    def pprint(self):
        super().pprint()
        Beta.pprint(self)
        Alpha.pprint(self)


if __name__ == '__main__':
    c = Charlie()
    c.pprint()
