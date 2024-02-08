"""
Created by Ignorant on 2024/2/7
Description: Other Introduction to Regular Expression
"""
import re

# class re.Match
match1 = re.search(r'h.*o', 'hello world')
print(match1.pos, match1.endpos, match1.span())
'''
group
    > use () to represent a group
    > default: one group
    > name the group: ?P<name>
'''
match2 = re.search(r'(2.*)(0.*)(0.*5)', 'aivasd2abva0iuwe0fjn5bk')
for i in range(4):
    print(match2.group(i))
print()

match3 = re.search(r'(?P<a>2.*)(?P<b>0.*)(?P<c>0.*5)', 'aivasd2abva0iuwe0fjn5bk')
print(match3.groupdict())
print(match3.groupdict()['a'])
print(match3.group(1))
print()

'''
method compile
    advantage: reuse the regular expression
'''
r = re.compile(r'f.*f')
print(r.search('afekufwc'))
print(r.search('sdfgfjsgmy'))
