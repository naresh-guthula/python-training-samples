# items = [(oct(item), hex(item), bin(item)) for item in range(1000000000000000000000000090)]

items = ((oct(item), hex(item), bin(item)) for item in range(3))

print(items)

# print(next(items))
# print(next(items))
# print(next(items))

for element in items:
    print(element)



