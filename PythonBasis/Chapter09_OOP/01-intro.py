"""
Created by Ignorant on 2024/2/1
Description: Introduction to OOP
"""


class Phone(object):
    # field
    brand = "huawei"
    price = 5000
    number = 18506258298

    # method
    def call(self):
        # print(self) ==> <__main__.Phone object at 0x000002573434EFA0>
        print("calling {}".format(self.number))


class Person(object):
    name = ''
    age = 0
    phone = Phone()


phone = Phone()
print(phone.brand)
phone.call()
print(phone.number)
phone.number = 13913610417
print(phone.number)
phone.call()

person1 = Person()
print(person1.name)
person1.name = "Carl"
print(person1.name)

Person.name = " "
person2 = Person()
print(person2.name)
