"""
Created by Ignorant on 2024/2/2
Description: __init__
"""


class Phone(object):
    # one of the magic methods: __init__(), serve as a constructor
    # magic method: __<method name>__(<arguments>)
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, name):
        print('{}: Calling {}'.format(self.brand, name))


phone = Phone('huawei', 5000)
print(phone.brand)
phone.call("Carl")
