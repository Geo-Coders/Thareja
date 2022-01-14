# Write a program to classify a given number as prime or composite

number= int(input('Enter number: '))
isComposite= 0
for i in range(2, number):
    if number % i == 0:
        isComposite = 1
        break

if isComposite == 1:
    print(f'{number} is a composite number')
else:
    print(f'{number} is a prime number')