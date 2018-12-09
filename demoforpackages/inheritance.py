class PackageManager:
    """
        demo for the Inheritance
    """

    def __init__(self, name, version):
        self.name = name
        self.version = version

    def get_information(self):
        print('name: ', self.name)
        print('version: ', self.version)

if __name__ == '__main__':
    pm = PackageManager('pip', '3.6.7')
    pm.get_information()
    # print(pm.name1)
    print(dir(pm))
