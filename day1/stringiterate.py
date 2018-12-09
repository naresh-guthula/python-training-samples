"""iterate the string"""

s = 'this is a template string is python'

for temp in s:
    if temp not in 'aeiou ': # membership test operator
        print(temp, ':', ord(temp))
