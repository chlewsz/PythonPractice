user0 = {
    'first_name': 'san',
    'last_name': 'zhang',
    'age': 30,
    'city': 'China'
}

user1 = {
    'first_name': 'si',
    'last_name': 'li',
    'age': 30,
    'city': 'China'
}

peoples = [user0, user1]
print(peoples)

for user in peoples:
    print(user['last_name'].title() + user['first_name'] + "'s age is" + str(user['age'])) 