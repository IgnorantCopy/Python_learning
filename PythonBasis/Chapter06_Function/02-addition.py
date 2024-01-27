"""
Created by Ignorant on 2024/1/24
Description: Addition for assigning
"""

# 装包
*a, b, c = 1, 2, 3, 4, 5
print(a, b, c)
a, *b, c = 1, 2, 3, 4, 5
print(a, b, c)
a, b, *c = 1, 2, 3, 4, 5
print(a, b, c)
print()

# 拆包
a, b, c = (1, 2, 3)
print(a, b, c)

# 拆 + 装
a, b, *c = (1, 2, 3, 4, 5)
print(a, b, c)
