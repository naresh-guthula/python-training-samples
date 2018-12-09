fp = open('password.txt')

# for temp in fp:
#    print(temp, end='')

occurrence={}
count = 0
for temp in fp:
    lastcol = temp.split(':')[-1]
    if lastcol.rstrip() in occurrence:
        occurrence[lastcol.rstrip()] = occurrence[lastcol.rstrip()] + 1
    else:
        count = 1
        occurrence[lastcol.rstrip()] = 1
print(occurrence)
fp.close()
