"""demo  for the IO"""

name = 'hp'
city = input('enter the city: ')
# no block level scoping, none similar to null
zip_code = None
try:
    zip_code = int(input('enter the postal code: '))
except ValueError as err:
    print('ddd')

print('name: ', name, sep='')
print('city: ', city, sep='')
print(zip_code)
print(type(zip_code))

# Out record separator
