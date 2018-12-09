from time import ctime, sleep

while True:
    with open('testit', 'a') as fw:
        fw.write(ctime + 'a dummy content' + '\n')

    sleep(.5)