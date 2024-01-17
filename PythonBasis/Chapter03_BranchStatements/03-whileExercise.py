"""
Created by Ignorant on 2024/1/17
Description: While Exercise
    Guess
"""

import random

# randint(self, a, b): Return random integer in range [a, b], including both end points.
num = random.randint(1, 100)
count = 0
while True:
    count += 1
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("You guessed!")
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")
print("You guessed %d times!" % count)
