purchase_ticket_message = 'Please input how old are you:'
purchase_ticket_message += '\n(input "quit" will break)'

while True:
    age = input(purchase_ticket_message)
    if age == 'quit':
        break
    else:
        try:
            if int(age) < 3:
                print('free')
            elif int(age) < 12:
                print('10 dollars')
            else:
                print('15 dollars')
        except ValueError:
            print('年龄输入错误')