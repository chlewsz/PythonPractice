while True:
    user_name = input("Please input your name:(input 'quit' will exit.)")

    if user_name == 'quit':
        break

    with open('guest_book.txt', 'a') as file:
        print('Hi ' + user_name)
        file.write(user_name + '\n')
