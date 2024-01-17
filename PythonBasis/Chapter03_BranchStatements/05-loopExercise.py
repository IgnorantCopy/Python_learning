"""
Created by Ignorant on 2024/1/17
Description: Loop Exercise
    掷两个骰子
    1.玩游戏需要金币
    2.开局赠金币10个
    3.玩一次消耗5个金币
    4.猜骰子大小，猜对得两个金币，猜错损失消耗的金币（超出6记作大，否则为小）
    5.游戏结束：主动结束或金币数不够
    6.结束时打印金币数和游戏共玩了几局
"""

import random

coins = 10
count = 0
while coins >= 5:
    char = input("(1) Start\n(2) Quit\n")
    if char == "2":
        break
    else:
        count += 1
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        guess = input("(1) big\n(2) small\n")
        if (guess == "1" and num1 + num2 > 6) or (guess == "2" and num1 + num2 <= 6):
            coins += 2
            print("You win! You still have %d coins." % coins)
        else:
            coins -= 5
            print("You lose!")
else:
    print("You do not have enough money to start another game!")
print("You have %d coins and you have played %d times" % (coins, count))
