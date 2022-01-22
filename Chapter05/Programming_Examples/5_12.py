# Write a program that greets a person

def greet(name, mesg):
# This function welcomes the person passed whose name is passed as parameter
    print('Welcome,' + name +',' + mesg)
mesg = 'Happy reading python is fun !'
name = input('\n Enter your name : ')
greet(name,mesg)