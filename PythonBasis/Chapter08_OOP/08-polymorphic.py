"""
Created bt Ignorant on 2024/2/4
Description: Polymorphic
"""


class Animal(object):
    def __init__(self, age):
        self.age = age


class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def feed_pet(self, pet):
        if isinstance(pet, Pet):
            print("{} is feeding {}".format(self.name, pet.nickname))
        else:
            print("it is not a pet!")


class Pet(Animal):
    def __init__(self, age, nickname, master):
        super().__init__(age)
        self.nickname = nickname
        self.master = master

    def eat(self, food):
        print("{} is eating {}...".format(self.nickname, food))


class Dog(Pet):
    def walk(self):
        print("{} is walking {}...".format(self.master.name, self.nickname))


class Cat(Pet):
    def catch(self):
        print("{} is catching mouse...".format(self.nickname))


class Tiger(Animal):
    @staticmethod
    def bite():
        print("tiger bites people")


person1 = Person("John", 25, 'M')
dog = Dog(2, "11", person1)
cat = Cat(3, "miao", person1)
tiger = Tiger(5)
person1.feed_pet(cat)
person1.feed_pet(tiger)
