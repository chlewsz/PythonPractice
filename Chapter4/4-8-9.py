cubs = []

for value in range(1, 11):
    cubs.append(value ** 3)

for value in cubs:
    print(value)

cubs_2 = [value ** 3 for value in range(1, 11)]
for value in cubs_2:
    print(value)