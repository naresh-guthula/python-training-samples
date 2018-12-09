def demo(value):
    value += 1


n = 10  # call by value
demo(n)
print(n)

n = [1, 3, 5]  # call by reference
