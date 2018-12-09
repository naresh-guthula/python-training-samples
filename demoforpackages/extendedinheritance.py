from demoforpackages.inheritance import PackageManager


class ExtendedPackageManager(PackageManager):
    """derived class"""

    # pass
    def __init__(self, name, version, arch, platform):
        self.arch = arch
        self.platform = platform
        super().__init__(name, version)  # invoking overridden method

    def get_information(self):
        super().get_information()
        print('system: ', self.arch)
        print('platform: ', self.platform)


if __name__ == '__main__':
    epm = ExtendedPackageManager('yum', '2.2.5', 'x86', 'drawin')
    epm.get_information()
