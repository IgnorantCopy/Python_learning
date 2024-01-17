"""
Created by Ignorant on 2024/1/15
Description: Variable
"""

'''
variable: function as a container
    > as a weak language, it is not strict to assign a value to a variable
'''
# integer
num1 = 0
print(type(num1))
# float
num2 = 1.0
print(type(num2))
# string
name = 'Carl'
print(type(name))
name = "Carl"
print(type(name))
name = '''
    I have a message
    I am Carl
'''
print(name)

word = "'Good luck', he said."
print(word)
word = '"Good luck", he said.'
print(word)

# boolean
isExist = True
print(type(isExist))
# a variable's type can be changed
isExist = 1
print(type(isExist))

# 竟然可以写中文！！！
# 年龄 = 18
# print(年龄)
