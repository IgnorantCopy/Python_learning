class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self, name, password):
        if name == self.name and password == self.password:
            print("Logged in successfully")
        else:
            print("Try Again")
