people_num = input('How many people? ')

try:
    if int(people_num) > 8:
        print('There no empty table')
    else:
        print('There are empty table')
except ValueError:
    print('无法转换成int')