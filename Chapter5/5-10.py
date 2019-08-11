current_users = ['John', 'Jack', 'lili', 'Jully', 'Bob']
new_users = ['Bob', 'Hong', 'Jack', 'Grace', 'Machiel']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + ' is used')
    else:
        print(new_user + " can use")
    
        