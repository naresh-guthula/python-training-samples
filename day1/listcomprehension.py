import csv
import collections
shells = [row[-1] for row in csv.reader(open('password.txt'), delimiter=':')]
shells1 = [row for row in csv.reader(open('password.txt'), delimiter=':')]

c = collections.Counter(shells)

for name, count in c.items():
    print(name, ':', count)