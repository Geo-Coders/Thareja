# Write a menu driven progam that keeps record of books
# journals available in a library

class Book:
    def __init__(self):
        self.title= ' '
        self.author= ' '
        self.price= 0

    def read(self):
        self.title= input('Enter Book Title: ')
        self.author= input('Enter Book Author : ')
        self.price= float(input('Enter Book Price : '))

    def display(self):
        print(f'Title {self.title}')
        print(f'Author : {self.author}')
        print(f'Price : {self.price}')
        print()

my_books= []
ch= 'y'
while ch == 'y':
    print('''
    1. Add New Book
    2. Display Books
    ''')
    choice= int(input('Enter choice : '))
    if choice == 1:
        book= Book()
        book.read()
        my_books.append(book)
    elif choice == 2:
        for i in my_books:
            i.display()
    else:
        print('Invalid Choice')

    ch= input('Do you want to continue... ')

print('Bye!')