"""
Created by Ignorant on 2024/1/21
Description: Inference of List
"""

list1 = ["list{}".format(i + 1) for i in range(10)]
print(list1)

list2 = [i for i in range(101) if i % 2 == 0]
print(list2)

list3 = ["3", "hello", "8", "world", "24"]
list4 = [i for i in list3 if i.isalpha()]
print(list4)

list5 = [i.title() if i.isalpha() and i.startswith('h') else i.upper() for i in list3]
print(list5)

list6 = [(i, j, k) for i in range(3) for j in range(3) for k in range(3)]
print(list6)

list7 = [list2[i:i + 3] for i in range(0, len(list2), 3) if i <= len(list2) - 3]
print(list7)
