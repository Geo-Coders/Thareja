# Write a program to return the full name of a person

from tkinter.ttk import Separator


def name(first_name, last_name):
    name_= f'{first_name} {last_name}'
    return name_

first_name= input('Enter your first name: ')
last_name= input('Enter your last name: ')

print(name(first_name, last_name))