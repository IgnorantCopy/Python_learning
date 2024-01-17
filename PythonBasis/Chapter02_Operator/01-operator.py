"""
Created by Ignorant on 2024/1/16
Description: Python Operator
"""

# 1.assigning operator: = += -= *= /= //= **= %=
a = 1
a += 1
b = 4
b -= 1
print(a, b)
print()

# 2.arithmetic operator: + - * / % ** //
num1 = a + b
num2 = a - b
num3 = a * b
num4 = a / b
num5 = a % b
num6 = a ** b    # 乘幂
num7 = a // b    # 整除
'''
print(self, *args, sep=' ', end='\n', file=None)
*args: the arguments to be printed
sep: the separator between arguments
end: the end of the line
file: file to the output(stdout if default)
'''
print(a, b, num1, num2, num3, num4, num5, num6, num7)
print()

# 3.relational operator: > < >= <= == != is
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print()

# comparison between strings
str1 = "abc"
str2 = "abd"
str3 = "bcd"
print(str1 > str2)
print(str1 > str3)
print(str2 > str3)
print()

# 4.logic operator: and or not
a = 0
print(a and b)
print(a or b)
print(not a)
print()

# 5.bit operator: & | ^ ~ << >>
n1 = 0b0110  # 6
n2 = 0b0010  # 2
print(n1 & n2)
print(n1 | n2)
print(n1 ^ n2)
print(~n1)
'''
6: 0000 0110
取反: 1111 1001
-1: 1111 1000
取反: 0000 0111   --> 7
'''
print(n2 >> 2)
print(n2 << 2)

'''
operator precedence
    1.**
    2.~ + -(一元加减)
    3.* / % //
    4.+ -
    5.>> <<
    6.&
    7.^ |
    8.<= < > >=
    9.<> == !=
    10.= += -= *= /= %= //= **=
    11.is/is not
    12.in/not in
    13.not > and > or
'''
