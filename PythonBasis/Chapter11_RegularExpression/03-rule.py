"""
Created by Ignorant on 2024/2/7
Description: Specific Rules of Regular Expression
"""
import re

'''
modifier
    S: let . match '\n'
    I: ignore case
    M: let $ match '\n'
'''
# S
print(re.search(r"j.*a", "sdjhvb\naave"))
print(re.search(r"j.*a", "sdjhvb\naave", re.S))
print()

# I
print(re.search(r"h", "ajHvr"))
print(re.search(r"h", "ajHvr", re.I))
print()

# M
print(re.findall(r'\w+$', 'i am a boy\n you are a girl\n he is a man'))
print(re.findall(r'\w+$', 'i am a boy\n you are a girl\n he is a man', re.M))
print()

# numbers and characters are themselves
# use \ before a special character to match itself
print(re.search(r"1\+2", "1+2"))
print()

r'''
special character: \
    1. \s: whitespace
    2. \S: opposite of \s
    3. \n: newline
    4. \t: tap
    5. \d: numbers  == [0-9]
    6. \D: opposite of \d   == [^0-9]
    7. \w: numbers, characters, Chinese and _
    8. \W: opposite of \w
'''
print('1.', re.search(r'\s', 'hello world'))
print('2.', re.search(r'\n', 'hello\nworld'))
print('3.', re.search(r'\t', 'hello\tworld'))
print('4.', re.search(r'\S', 'hello world'))
print('5.', re.search(r'\d', 'hello0world'))
print('6.', re.search(r'\D+', 'he110'))
print('7.', re.findall(r'\w+', '---he110_.*world---'))
print('8.', re.findall(r'\W+', '---he110_.*world---'))
print()

'''
other special characters
    1.(): divide groups
    2. .: any character except '\n'
    3.[]: selection scope
    4.|: or
    5.{}: number of time
        {n}: n times
        {a, b}: [a, b] times
        {n,}: >= n times
        {, n}: <= n times
    6.*: the character before can occur any time
    7.+: the character before should occur at least once    == {1,}
    8.?:
        ① the character before should occur no more than once   =={, 1}
        ② greedy mode ==> non-greedy mode
    9.^: start with
    $: end with
'''
print('3.', re.search(r'f[0-5]m', 'asdhjcbf5maec'))
print('3.', re.search(r'f[0-5a-dx]m', 'asdhjcbf5cmaec'))  # [0-5a-dx] ==> 0-5 or a-d or x
print('4.', re.search(r's(abc|cd)v', 'ascdvbt'))
print('5.', re.search(r'x{2}', 'guxmguawrxxfrx'))
print('5.', re.search(r'x{2,}', 'guxmguawrxxcxxxxfrx'))
print('5.', re.search(r'x{2,}', 'guxmguawrxxxxxxfrx'))
print('5.', re.search(r'x{,2}', 'guxmguawrxxfrx'))
print('5.', re.search(r'x{1,2}', 'guxmguawrxxfrx'))
print('5.', re.search(r'x{1,2}', 'guxxmguawrxxfrx'))
print('6.', re.search(r'go*d', 'goooood'))
print('7.', re.search(r'go+d', 'goooood'))
print('8.', re.search(r'go?d', 'gd'))
print('9.', re.search(r'^a.*z$', 'abcdxyz'))
print()

'''
greedy mode and non-greedy mode
    > greedy mode(default): match as much as possible
    > non-greedy mode: match as less as possible
'''
# greedy mode
print(re.search(r'm.*a', 'avcmekuaxsa').group())
# non-greedy mode
print(re.search(r'm.*?a', 'avcmekuaxsa').group())
print()

x1 = re.match(r'aa(\d+)', 'aa2243ddd')
print(x1.group(0))
print(x1.group(1))
x2 = re.match(r'aa(\d+?)', 'aa2243ddd')
print(x2.group(0))
print(x2.group(1))
print()

x3 = re.match(r'aa(\d+)ddd', 'aa2243ddd')
print(x3.group(0))
print(x3.group(1))
x4 = re.match(r'aa(\d+?)ddd', 'aa2243ddd')
print(x4.group(0))
print(x4.group(1))
print()

x5 = re.match(r'aa(\d+?).*', 'aa243ddd')
print(x5.group(0))
print(x5.group(1))
x6 = re.match(r'aa(\d??)(.*)', 'aa243ddd')
print(x6.group(0))
print(x6.group(1))
print(x6.group(2))
