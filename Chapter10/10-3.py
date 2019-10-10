user_name = input('Please input your name: ')
with open('guest.txt', 'w') as file:
    file.write(user_name)
