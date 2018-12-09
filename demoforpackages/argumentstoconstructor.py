"""
    PackageManager

    name
    version
"""


class PackageManager:
    """
        demo for the access specifier
    """
    __name1 = 'abc'  # private attribute

    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __get_information(self):
        print('name: ', self.name)
        print('version: ', self.version)

    def wrapper(self):
        """ public method"""
        self.__get_information()


if __name__ == '__main__':
    pm = PackageManager('pip', '3.6.7')
    pm.wrapper()
    # print(pm.name1)
    print(dir(pm))
