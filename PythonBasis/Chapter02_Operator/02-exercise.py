"""
Created by Ignorant on 2024/1/16
Description: Exercise 02
    键盘输入一个3位整数,打印个位数、十位数、百位数
"""

x = int(input("Please enter a three-digit number: "))
ge = x % 10
shi = x // 10 % 10
bai = x // 100 % 10
# printf
print("个位:%d, 十位:%d, 百位:%d" % (ge, shi, bai))