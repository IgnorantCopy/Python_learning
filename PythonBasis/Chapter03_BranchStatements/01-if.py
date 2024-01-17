"""
Created by Ignorant on 2024/1/17
Description: if statement
"""
import random

score = int(input("please enter your score: "))
if score < 60:
    print("不及格")
elif score < 80:
    print("良好")
else:
    print("优秀")

'''
Exercise 01
    一个四位整数，每位加和如果大于10，打印success，否则打印fail
'''
number = int(input("please enter a four-digit number: "))
if number // 1000 % 10 + number // 100 % 10 + number // 10 % 10 + number % 10 > 10:
    print("success")
else:
    print("fail")

'''
Exercise 02
    购物节：输入购买总金额，
    如果金额 0 ~ 500 则为Lv.1
    如果金额 500 ~ 2000 则为Lv.2
    2000 以上为Lv.3
    Lv.1: 随机赠送3张 1 ~ 10 元优惠券
    Lv.2: 赠送2张50元优惠券，如果充值则送充值金额的10%
    Lv.3: 赠送2张100元优惠券，如果充值则送充值金额的15%
'''

money = int(input("please enter your sum of consumption: "))
balance = 5000
coupon = 0
if money <= 500:
    coupon1 = random.randint(1, 10)
    coupon2 = random.randint(1, 10)
    coupon3 = random.randint(1, 10)
    coupon = coupon1 + coupon2 + coupon3
elif money <= 2000:
    coupon = 2 * 50
    isRecharge = input("would you like to recharge some money? (y/n): ")
    if isRecharge == "y":
        recharge = int(input("how much money would you like to recharge: "))
        coupon += recharge * 0.1
else:
    coupon = 2 * 100
    isRecharge = input("would you like to recharge some money? (y/n): ")
    if isRecharge == "y":
        recharge = int(input("how much money would you like to recharge: "))
        coupon += recharge * 0.15
