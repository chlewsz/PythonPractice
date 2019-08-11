names = ['John', 'Jack', 'lili', 'Admin', 'Bob']

if names:
    for name in names:
        if name.lower() == 'admin':
            print('hello admin, would you like to see a status report?')
        else:
            print('Hello ' + name + ", thank you for logging in again")
else:
    print('we need to find some users')