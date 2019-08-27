from restaurant import Restaurant

# restaurant = Restaurant('冷面', 'a')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.read_number_served()

# restaurant.set_number_served(100)
# restaurant.read_number_served()
# restaurant.increment_number_served(10)
# restaurant.read_number_served()

class IceCreamStand(Restaurant):
    def __init__(self,  restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ice', 'hot', 'water']

    def desc_flavors(self):
        desc = 'Have some flavors like: '
        for flavor in self.flavors:
            desc += flavor + ', '
        print(desc[: -2])

icecream_stand = IceCreamStand('ice', 'a')
icecream_stand.desc_flavors()

