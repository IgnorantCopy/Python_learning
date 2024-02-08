"""
Created by Ignorant on 2024/2/7
Description: Regular Expression Operation
"""
import re
from collections.abc import Iterable

'''
find
    1.match(pattern, string, flags=0)
        Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.

    2.search(pattern, string, flags=0)
        Scan through string looking for a match to the pattern, returning a Match object, or None if no match was found.
    
    3.finditer(pattern, string, flags=0)
        Return an iterator over all non-overlapping matches in the string.
        For each match, the iterator returns a Match object.

        Empty matches are included in the result.
    
    5.fullmatch(pattern, string, flags=0)
        Try to apply the pattern to all of the string, returning a Match object, or None if no match was found.
'''
message1 = "hello world hello"
message2 = "\\\\"
# r before the str means original str
print(re.search(r"\\", message2))
print(re.search("\\\\", message2))
print()
# differences between match and search
print(re.match(r"hello", message1))
print(re.search(r"hello", message1))
print(re.match(r"world", message1))
print(re.search(r"world", message1))
print()

list1 = re.finditer(r'x', 'sfdbxavfxxvffaddxavnygvxjkdsi')
print(isinstance(list1, Iterable))
print(list1)
for i in list1:
    print(i)
print()

list2 = re.findall(r'x\d+', 'sfdbx12avfx5xvffaddx80avn47ygvx21jkdsi')
print(list2)
print()

message3 = "hello world"
print(re.fullmatch(r"hello", message3))
print(re.fullmatch(r"hello world", message3))
print(re.fullmatch(r'h.*d', 'hshbdvuqewfd'))
print()

'''
replace
    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost non-overlapping occurrences of
        the pattern in string by the replacement repl. 
        repl can be either a string or a callable:
            if a string, backslash escapes in it are processed.
            if a callable, it's passed the Match object and must return a replacement string to be used.
'''
print(re.sub(r'\d', 'x', '1b2m3a4d5b6v7e8u9r0'))
# double the number in the str
message4 = 'hello23world34'
print(re.sub(r"\d+", lambda s: str(int(s.group(0)) * 2), message4))
