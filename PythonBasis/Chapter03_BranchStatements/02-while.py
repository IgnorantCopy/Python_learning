"""
Created by Ignorant on 2024/1/17
Description: while statement
"""

# 输入账号密码，有3次试错机会
trial = 3
while trial:
    account = input("please enter your account: ")
    password = input("please enter your password: ")
    if account == "Ignorant" and password == "12345":
        print("login successfully")
        break
    else:
        print("wrong password or account name")
        trial -= 1
if trial == 0:
    print("you waste all chances")

'''
Exercise
    超市买东西，输入商品价格和数量，计算所有所需支付的金额
'''
sum = 0
count = 1
while count != 6:
    money = int(input("enter the price of good%d: " % count))
    num = int(input("enter the quantity of good%d: " % count))
    sum += money * num
    count += 1
    answer = input("do you want to add another good?(y/n)")
    if answer == "n":
        break
print(sum)
