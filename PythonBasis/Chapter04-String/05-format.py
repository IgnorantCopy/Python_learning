"""
Created by Ignorant on 2024/1/18
Description: Formatting Strings
"""

name = "Carl"
age = 18

# {} placeholder
print("My name is {} and I am {} years old.".format(name, age))

# use index
print("He is {0} years old and I am {0} years old too.".format(age))

# use variable
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
