"""
Created by Ignorant on 2024/1/15
Description: Type Transfer
"""

# input(): blockage function
name = input("please enter your name: ")
age = int(input("please enter your age: "))
print("your name is " + name + " and your age is " + str(age))

# a string with decimal point cannot be transferred to an integer, but a float can
# num = "12.9"
# print(int(num))
num = 12.9
print(int(num))

flag = True
print(int(flag))
print(str(flag))
# in Python, only 0 "" '' None () {} [] will be transferred to False
print(bool(5))
print(bool(0))
print(bool(''))
