import re

s = 'the python and the perl scripting'
pattern = 'P.+N'  # greedy match
pattern = 'P.+?N'  # non greedy match

m = re.search(pattern, s, re.I)
print(m)

if m:
    print('match string: ', m.group())
    print(m.start())
    print(m.end())
    print('before: ', s[:m.start()])
    print('after: ', s[m.end():])
else:
    print('failed to match')



# multiple matches

for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
    print()

print(re.findall(pattern, s, re.I))