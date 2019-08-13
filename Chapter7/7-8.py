sandwich_orders = ['tuna', 'pastrami', 'vegatables', 'pastrami', 'meat', 'pastrami']
finished_sandwiches = []

print('pastrami sell out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)