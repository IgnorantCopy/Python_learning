"""
Created by Ignorant on 2024/1/18
Description: Common String Operations1
"""

path = "https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E7%83%AD%E6%90%9C&sa=ire_dl_gh_logo_texing&rsv_dl=igh_logo_pc"
# len(str): return the length of a string
print(len(path))
print()

'''
search
    1.find(self, sub, start=None, end=None): 
        Return the lowest index in String where substring sub is found,
        such that sub is contained within String[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
    
    2.rfind(self, sub, start=None, end=None): 
        Return the highest index in String where substring sub is found,
        such that sub is contained within String[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
    
    3.index(self, sub, start=None, end=None):
        Return the lowest index in String where substring sub is found,
        such that sub is contained within String[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
    
    4.rindex(self, sub, start=None, end=None):
        Return the highest index in String where substring sub is found,
        such that sub is contained within String[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
'''
index1 = path.find('?')
print(index1)
print(path[:index1])

index2 = path.rfind('=')
print(index2)
print(path[index2 + 1:])

'''
count(self, sub, start=None, end=None):
    Return the number of non-overlapping occurrences of substring sub in
    string String[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
'''
print(path.count('_'))
print()

'''
judge
    1.startswith(self, prefix, start=None, end=None):
        Return True if String starts with the specified prefix, False otherwise.
        With optional start, test String beginning at that position.
        With optional end, stop comparing String at that position.
        prefix can also be a tuple of strings to try.
        
    2.endswith(self, suffix, start=None, end=None):
        Return True if String ends with the specified suffix, False otherwise.
        With optional start, test String beginning at that position.
        With optional end, stop comparing String at that position.
        suffix can also be a tuple of strings to try.
        
    3.isalpha(self, *args, **kwargs):
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        
    4.isdigit(self, *args, **kwargs):
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        
    5.isalnum(self, *args, **kwargs):
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        
    6.isspace(self, *args, **kwargs):
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
    7.islower(self, *args, **kwargs):
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        
    8.isupper(self, *args, **kwargs):
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
'''
print(path.startswith("https"))
print(path.endswith(".png"))
print()

str1 = "abc123"
str2 = "    "
print(str1.isalpha())
print(str1.isdigit())
print(str1.isalnum())
print(str2.isspace())
print()

str3 = "hello"
str4 = "ABC"
print(str1.islower())
print(str3.islower())
print(str4.isupper())

