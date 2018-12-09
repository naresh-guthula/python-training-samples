def log_watch(file_name):
    try:
        with open(file_name) as fp:
            fp.seek(0, 2)

            while True:
                content = fp.read()
                if content:
                    yield content
    except(FileNotFoundError, IOError) as err:
        print(err)


if __name__ == '__main__':
    for lines in log_watch('testit'):
        print(lines)
