"""
Created by Ignorant on 2024/1/17
Description: for statement
"""

'''
format:
    for i in range(n):
        ...
    
    range(stop) / range(start, stop) / range(start, stop, step)
        Return an object that produces a sequence of integers from start (inclusive) (0 if default)
        to stop (exclusive) by step (1 if default)
    
    for i in String:
        ...
    i: the character in String
'''

for i in range(1, 11, 2):
    print(i)

for i in "3jh4bl3b54":
    if i.isdigit():
        print(i, end = ' ')
print()

# rewrite the first code in 02-while.py
'''
for-else statement:
    for i in range(n):
        ...
    else:
        ...
if break is executed, the codes in else will be executed
in a similar way, there is while-else statement
'''
for i in range(3):
    account = input("please enter your account: ")
    password = input("please enter your password: ")
    if account == "Ignorant" and password == "12345":
        print("login successfully")
        break
    print("wrong password or account name\n")
else:
    print("you waste all chances")
