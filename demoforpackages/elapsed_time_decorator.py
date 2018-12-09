from time import perf_counter, sleep


class NegativeDelayError(Exception):
    pass


def time_it(func):
    def time_it_handler(*args):
        ts = perf_counter()
        value = func(*args)
        print('elapsed time : ', perf_counter() - ts)
        return value

    return time_it_handler


class Custom:
    @time_it
    def execute(self, delay):
        if delay < 0:
            raise NegativeDelayError('time delay cant be a negative value: {}'.format(delay))
        sleep(delay)


if __name__ == '__main__':
    c = Custom()

    c.execute(3)
    c.execute(-3)
    print()
