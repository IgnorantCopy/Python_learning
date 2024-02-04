"""
Created by Ignorant on 2024/1/29
Description: Raise Exception
"""

name = input("Please enter your name longer than 6 characters: ")
try:
    if len(name) < 6:
        raise Exception("Please enter your name longer than 6 characters")
    else:
        print("Your name is", name)
except Exception as e:
    print(e)
