"""
Created by Ignorant on 2024/1/18
Description: Common String Operations2
"""

str1 = "Hello World! Hello Python!"
'''
replace(self, __old, __new, __count):
    Return a copy with all occurrences of substring old replaced by new.
    
        count:
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
    
    If the optional argument count is given, only the first count occurrences are
    replaced.
'''
str2 = str1.replace("Hello", "#￥%……&*", 1)
print(str2)
print()

'''
cutting
    1.split(self, sep, maxsplit):
        Return a list of the words in the string, using sep as the delimiter string.
        
        sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
        maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
    
    2.splitlines(self, keepends):
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
    
    3.partition(self, __sep):
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
'''
result = str1.split(' ', 2)
print(result)
str3 = """
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
"""
result = str3.splitlines()
print(result)

result = str1.partition(' ')
print(result)
print()

'''
capital
    1.title(self):
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
    
    2.upper(self): Return a copy of the string converted to uppercase.
    
    3.lower(self): Return a copy of the string converted to lowercase.
    
    4.capitalize(self): 
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower case.
'''
str4 = "hello world"
print(str4.title())
print(str4.upper())
print(str4.lower())
print(str4.capitalize())
print()

'''
space process
    1.strip(self, chars):
        Return a copy of the string with leading and trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
    
    2.lstrip(self, chars):
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
    
    3.rstrip(self, chars):
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
'''

str5 = "  admin    "
str6 = "aadmina"
print(str5.strip())
print(str6.strip('a'))
print(len(str5.strip()))
print(len(str5.lstrip()))
print(len(str5.rstrip()))
print()

'''
align
    1.center(self, __width, __fillchar):
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
    
    2.ljust(self, __width, __fillchar):
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
    
    3.rjust(self, __width, __fillchar):
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
'''
print(str4.center(50, '*'))
print(str4.ljust(50, '*'))
print(str4.rjust(50, '*'))

'''
join(self, ab=None, pq=None, rs=None):
    Concatenate any number of strings.
        
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
'''
str7 = " "
str_list = ["Hello", "World", "!"]
print(str7.join(str_list))
