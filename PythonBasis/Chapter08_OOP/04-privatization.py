"""
Created by Ignorant on 2024/2/4
Description: Privatization
"""


class Person(object):
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.__gender = gender

    # packaging
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # decorator
    @property
    def gender(self):
        return self.__gender

    # first getter, then setter
    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def __str__(self):
        return "class Person:{}".format(dict([("name", self.__name), ("age", self.age), ("gender", self.__gender)]))


person1 = Person("Carl", 30, 'M')
print(person1.get_name())
person1.gender = 'F'
print(person1.gender)

'''
dir(__o: object = ...) -> list[str]

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes of the given object,
and of attributes reachable from it. If the object supplies a method named __dir__, it will be used;
otherwise the default dir() logic is used and returns:

    > for a module object: the module's attributes.
    > for a class object: its attributes, and recursively the attributes of its bases.
    > for any other object: its attributes, its class's attributes, and recursively the attributes of
                            its class's base classes.
'''
print(dir(Person))
print(dir(person1))
