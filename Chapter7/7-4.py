message = 'Please add pizza topping:'
message += '\n(input "quit" will break)'

while True:
    topping = input(message)

    if topping == 'quit':
        break
    else:
        print('adding ' + topping)

