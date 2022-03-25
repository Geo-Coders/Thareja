# Make a class Book with members, title, author,publisher and isbn number
# The functions of the class should read and display the data

class Book:
    def __init__(self):
        self.title = ' '
        self.author = ' '
        self.publisher = ' '
        self.ISBN = 0
        
    def read(self):
        self.title = input('Enter the book title : ')
        self.author = input('Enter the name of the author : ')
        self.publisher = input('Enter the publisher name : ')
        self.ISBN = int(input('Enter the ISBN number : '))
        
    def display(self):
        print(f'Title : {self.title} Author : {self.author} Publisher : {self.publisher} ISBN Number : {self.ISBN}')
        
B = Book()
B.read()
B.display()
