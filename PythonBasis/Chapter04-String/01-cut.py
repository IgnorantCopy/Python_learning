"""
Created by Ignorant on 2024/1/18
Description: String Cut
"""

str = "ABCDEFG"
'''
index
    positive index: 0 ~ len(str) - 1
    negative index: -len(str) ~ -1
'''
print(str[3], str[-4])
print()

'''
slice
    str[start_index:end_index(:step)]
    start_index: 0 if default (inclusive)
    end_index: len(str) if default (exclusive)
    step:
        positive: left to right
        negative: right to left
'''
print(str[1:4])
print(str[:4])
print(str[1:])
print(str[:])
print(str[::2])
print(str[::-2])
# print(str1[0:6:-2])   ==> X
print(str[6::-2])
