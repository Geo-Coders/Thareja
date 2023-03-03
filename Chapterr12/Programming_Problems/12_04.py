# A program that prompts the user to enter his name
# The program then greets the person with his name
# But if the person's name is Rahul an exception is thrown and he is asked to quit the program

print('--- A Program to greet a person and throw exception when the name Rahul is used---')
print()

try:
    name = input("Please enter your name : ")
    if name == "Rahul":
        raise NameError
except NameError:
    print('Please quit the program!')
    
else:
    print("Hello" +" ", name)
        