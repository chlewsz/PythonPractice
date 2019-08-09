cubs = [value ** 3 for value in range(1, 11)]

print('The first three items in the list are:')
print(cubs[:3])

print('Three item from the middle of the list are:')
print(cubs[int(len(cubs) / 2 - 1):int(len(cubs) / 2 + 2)])

print('The last three items in the list are:')
print(cubs[-3:])