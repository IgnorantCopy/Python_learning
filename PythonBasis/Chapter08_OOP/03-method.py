"""
Created by Ignorant on 2024/2/2
Description: Method
"""


class Person(object):
    # add double _ before id to privatize it
    __id = 1000

    # 1.magic method
    # __init__(): do while initializing an object
    def __init__(self, name, age, gender):
        print("init...")
        self.add_id()
        self.name = name
        self.age = age
        self.gender = gender

    # __new__(): do while instantiating an object
    def __new__(cls, *args, **kwargs):
        print("new...")
        return super().__new__(cls)

    # __call__(): do while calling an object
    def __call__(self, *args, **kwargs):
        print("call...")

    # __del__(): destruct magic method. do only once no matter how many times you use it
    #           after finishing using the address while deleting the reference of an object
    #           In other words, do while python interpreter frees the memory of the object
    # do not recommend to rewrite it
    def __del__(self):
        print("del...")

    # __str__(): the same as toString() in java
    def __str__(self):
        return "class Person: {}".format(dict([("name", self.name), ("age", self.age), ("gender", self.gender)]))

    # 2.common method
    def eat(self, food):
        print("{} is eating {}".format(self.name, food))

    '''
    3.class method
        > rely on the decorator @classmethod
        > the first argument of class method is not a object, but a class
        > only class fields and class methods can be used in a class method
        > function of class method: do something while initializing
    '''

    @classmethod
    def add_id(cls):  # cls: class
        # print(cls) ==> <class '__main__.Person'>
        cls.__id += 1

    @classmethod
    def get_id(cls):
        return cls.__id

    '''
    4.static method
        > rely on the decorator @staticmethod
        > do not need cls and self
        > only class fields and class methods can be used in a static method
        > function of class method: do something while initializing
    '''

    @staticmethod
    def update_id(new_id):
        Person.__id = new_id

    '''
    class method VS static method
        similarity:
            > only class fields and class methods can be used
            > can be used through class name
            > do not rely on objects
        difference:
            > different decorator
            > class method must have the argument cls, static method need not any
    
    common method VS class method & static method
        similarity:
            > 
            > 
        difference: 
            > common method does not have decorator
            > common method relies on objects
            > common methods can be used only after initializing a object
    '''


'''
instantiation
    1.__new__()
    2.__init__()
    constructor: 1 + 2
'''
person1 = Person('Carl', 18, 'M')
person1()
person1.eat('Banana')
person2 = person1
del person2
print(person1.name)
print(person1)
Person.add_id()
print(Person.get_id())
Person.update_id(1000)
print(Person.get_id())
