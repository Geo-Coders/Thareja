# Write an interactive program to read an integer
# If it is positive then display the corresponding binary representation of that number
# The user must enter 999 to stop.
# Incase the user enters a negative number, then ignore that input and ask the user to re-enter any different number
print('----- A program to display the binary representation of a given positive integer ------')
print()
print('Enter 999 to Exit')
int_num = 0
binary_num = '0'
while int_num !=999:
    int_num = int(input('Enter the integer : '))
    
    if int_num >= 1:
    
        if int_num % 2 == 0:
            binary_num = binary_num + '0'
            int_num = int_num / 2
            print(f'The binary equivalent = {binary_num}')
            
        else:
            binary_num = binary_num + '1'
            int_num = (int_num - 1)/ 2
            print(f'The binary equivalent = {binary_num}')
    
    else:               
        print('Re-enter any different number')
    

   
    