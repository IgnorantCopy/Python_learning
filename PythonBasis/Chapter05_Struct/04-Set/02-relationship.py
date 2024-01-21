"""
Created by Ignorant on 2024/1/21
Description: Relationship Between Sets
"""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8, 9}
# 交集: intersection / &
result = set1.intersection(set2)
print(result)
print(set1 & set2)

# 并集: union / |
result = set1.union(set2)
print(result)
print(set1 | set2)

# 差集: difference / -
result = set1.difference(set2)
print(result)
print(set1 - set2)
result = set2.difference(set1)
print(result)
print(set2 - set1)

# 差集的并集
print(set1 ^ set2)
