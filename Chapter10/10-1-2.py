file_name = 'learning_python.txt'

with open(file_name) as file:
    contents = file.read()
    print(contents.rstrip())

with open(file_name) as file:
    for line in file:
        print(line.rstrip().replace('Python', 'C'))

with open(file_name) as file:
    contents = file.readlines()

for line in contents:
    print(line.rstrip())
