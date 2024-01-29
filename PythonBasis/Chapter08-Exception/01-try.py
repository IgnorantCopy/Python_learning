"""
Created by Ignorant on 2024/1/29
Description: try-except block
"""

try:
    n1 = int(input('Enter a number: '))
    n2 = int(input('Enter another number: '))
    operator = input('Enter the operation(+ - * /): ')
    if operator == '+':
        print(n1 + n2)
    elif operator == '-':
        print(n2 - n1)
    elif operator == '*':
        print(n1 * n2)
    elif operator == '/':
        print(n1 / n2)
    else:
        print('Invalid input!')
except ZeroDivisionError:
    print("Divided by zero!")
except ValueError:
    print("Invalid input!")
except Exception:
    pass
else:
    print("No exception occurred!")
finally:
    print('Goodbye!')
print()


def func():
    fis = None
    try:
        fis = open("../Chapter07-File/data/a.txt", 'r')
        print(fis.read())
        return 1
    except FileNotFoundError as e:
        print(e)
        return 2
    finally:
        print("-----finally-----")
        if fis is not None:
            fis.close()
        return 3


print(func())
