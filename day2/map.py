items = [1, 2, 3]

m = map(hex, items)

print(m)

for item in m:
    print(item)

m = map(ord, 'peter pan')
print(list(m))

add_one = lambda a: a + 2

power = lambda a,b: a **b

print(list(map(add_one, items)))
print(list(map(power, items, [2,3,4])))



