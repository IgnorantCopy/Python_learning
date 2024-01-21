"""
Created by Ignorant on 2024/1/20
Description: Exercise - Dictionary
    添加书：要求不能添加重名的书
"""

books = []
while True:
    if len(books) == 4:
        print("The books are full")
        break
    name = input('please enter the name of the book: ')
    for i in books:
        if i['name'] == name:
            print("The book is already exist")
            isExist = True
            break
    price = float(input('please enter the price of the book: '))
    author = input('please enter the author of the book: ')
    isExist = False
    if not isExist:
        books.append({"name": name, "price": price, "author": author})
    answer = input("Do you want to add another book?(y/n): ")
    if answer.lower() == 'n':
        break
print(books)
