"""
Created by Ignorant on 2024/1/31
Description: Inference of Dictionary
"""

dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}
dict2 = {k: v for v, k in dict1.items()}
print(dict2)
