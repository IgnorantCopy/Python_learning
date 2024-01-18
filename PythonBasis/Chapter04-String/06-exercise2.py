"""
Created by Ignorant on 2024/1/18
Description: Exercise 2
    用户发言
    要求：
    1.内容不为空（不全为空格）
    2.最多发言20个字
    3.无敏感词汇
    4.内容前后无空格
"""

name = input('Enter your name: ')
while True:
    contents = input('Enter your contents: ')
    contents = contents.strip()
    if len(contents) == 0:
        print("Your contents are empty!")
    elif len(contents) > 20:
        print("Your contents' length is too long!")
    else:
        contents = contents.replace("fuck", "****")
        break
print("{}: ".format(name) + contents)
