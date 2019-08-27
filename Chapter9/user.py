class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print('login attemps is ' + str(self.login_attempts))

    def describe_user(self):
        print(self.first_name + self.last_name + "'s sex is " + self.sex + ' and age is ' + str(self.age))

    def greet_user(self):
        print('hi ' + self.last_name)
