# Write a program to read two numbers. 
# Then find out whether the first number is a multiple of the second number

print('--- A Program to evaluate whether a number is a multiple of the another ---')
print()

x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))

try:
    if x % y == 0:
        print(f"\nThe number {x} is a multiple of {y}")
    else:
        print(f"The number {x} is not a multiple of {y}")

except ZeroDivisionError:
    print(f"Please enter a non zero number for the Second number instead of {y}")