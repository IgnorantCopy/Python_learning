"""
Created by Ignorant on 2024/2/4
Description: Inheritance
"""


class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print("{} is running...".format(self.name))

    def eat(self):
        print("{} is eating...".format(self.name))


'''
class super(object):
    super() -> same as super(__class__, <first argument>)
    super(type) -> unbound super object
    super(type, obj) -> bound super object; requires isinstance(obj, type)
    super(type, type2) -> bound super object; requires issubclass(type2, type)
    Typical use to call a cooperative superclass method:
    class C(B):
        def meth(self, arg):
            super().meth(arg)
    This works for class methods too:
    class C(B):
        @classmethod
        def cmeth(cls, arg):
            super().cmeth(arg)
'''


class Student(Person):
    def __init__(self, name, age, gender, grade, score):
        super().__init__(name, age, gender)
        self.grade = grade
        self.score = score

    def eat(self, food="rice"):
        print("{} is eating {}...".format(self.name, food))


class Doctor(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary

    def eat(self, food="rice"):
        print("{} is eating {}...".format(self.name, food))


class Dentist(Doctor):
    def __init__(self, name, age, gender, salary, patients):
        super().__init__(name, age, gender, salary)
        self.patients = patients

    def check(self):
        print("----------Checking Patients----------")
        for patient in self.patients:
            print("{} is checking {}...".format(self.name, patient.name))
        print("---------------Finish---------------")


student1 = Student('Carl', 20, 'M', 14, 100)
doctor1 = Doctor('Jack', 35, 'M', 10000)
person1 = Person("Rose", 20, 'F')
dentist1 = Dentist('Jones', 30, 'M', 25000, [student1, person1])
person1.eat()
student1.run()
doctor1.eat("fish")
dentist1.check()
