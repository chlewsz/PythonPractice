class Restaurant():
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number

    def read_number_served(self):
        print("number served is " + str(self.number_served))

    def describe_restaurant(self):
        print("name is " + self.restaurant_name + " type is " + self.cuisine_type)

    def open_restaurant(self):
        print("open restaurant")