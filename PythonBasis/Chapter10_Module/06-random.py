"""
Created by Ignorant on 2024/2/6
Description: Module random
"""
import random

# random.random(): Return a random float in the interval [0, 1)
print(random.random())
'''
randrange(self, start, stop=None, step=1)
    Choose a random item from range(start, stop[, step]).

    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.
'''
print(random.randrange(1, 50, 2))

# randint(self, a, b): Return random integer in range [a, b], including both end points
print(random.randint(1, 10))

'''
choice(self, seq)
    Choose a random element from a non-empty sequence
    raises IndexError if seq is empty
'''
list1 = ["Carl", "Jack", "Merry", "Keven", "Rose"]
print(random.choice(list1))

'''
shuffle(self, x, random=None)
    Shuffle list x in place, and return None.

    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.
'''
random.shuffle(list1)
print(list1)
