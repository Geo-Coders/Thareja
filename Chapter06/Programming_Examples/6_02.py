# Write a program that takes user's name and PAN card number as input
# Validate the information using isX function and print the details
while(1):
    name = input('\n Enter your name : ')
    if name.isalpha() == False:
        print('Invalid Name, Sorry you cannot proceed.')
        break
    else:
        pan_card_no = input('\n Enter your PAN card number : ')
        if pan_card_no.isalnum() == False:
            print('Invalid PAN card Number, Sorry you cannot proceed')
            break
        print(f'Please check {name} your PAN card number is : {pan_card_no}')
        break