def make_pizza(*toppings):
    for topping in toppings:
        print('- ' + topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')