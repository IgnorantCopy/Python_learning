"""
Created by Ignorant on 2024/2/5
Description: Introduction to Module
"""
import calculate
import myPackage
# from calculate import *
from myPackage.model import User

'''
模块(module)是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个.py文件就是一个模块，模块名就是文件名(不含后缀)
好处:
    > 提高了代码的可复用性、可维护性
    > 解决了命名冲突,不同模块中相同的命名不会冲突
'''

list1 = [1, 2, 3, 4, 5]
print(calculate.add(*list1))
print(calculate.minus(*list1))
print(calculate.multiply(*list1))
print(calculate.divide(*list1))
calculator = calculate.Calculator(calculate.PI)
calculator.test()
print()

user = User("Admin", "123456")
user.login("Admin", "123456")
myPackage.create()
