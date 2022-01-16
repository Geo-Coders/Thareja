# Write a program to determine whether a person is eligble to vote or not. if he is not eligble, display how many years are left to be eligble.

age= int(input('Enter the age: '))
if age >= 18:
    print('You are eligible to vote')
    
yrs= 18 - age
print(f'You have to wait for another {yrs} years to cast your vote')
