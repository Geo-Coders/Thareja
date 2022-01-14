#----- program 4.6 -----
# Write a program to enter any character. if the enteres character is in lowercase then convert it into uppercase and if it is an uppercase, the  convert it into lowercase
ch = input('Enter any character : ')
if ch >= 'A' and ch <= 'Z':
    ch = ch.lower()
    print('The entered character was in uppercase. In lowercase it is : '+ ch)
else:
    ch = ch.upper()
    print('The entered character was in lowercase. In upperrcase it is : '+ ch)