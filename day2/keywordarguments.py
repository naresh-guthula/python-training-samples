"""keywor arguments functions"""


def tuner(**kwargs):
    print(kwargs)


tuner()
tuner(contract=0.8, brightness=0.79, hue=0.85)
param = dict(contract=0.8, brightness=0.79, hue=0.85)
tuner(**param) # passing a dict content as an argument to the keyword args
