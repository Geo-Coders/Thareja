# Write a function called printStatus that is passed status code
# 'S', 'M', 'D', or 'U' and returns the string 'SEPARATED', 'MARRIED',
# 'DIVORCED', or 'UNMARRIED', respectively. In case an inappropriate letter is passed,
# print an appropriate message. Also include a docstring with your function.

print('--- A Program to check Marital Status of the user ---')
print()

def printStatus(input_):
    ''' A function that returns the marital status from the given initial '''
    dict_status= {
        'S':'SEPARATED',
        'M':'MARRIED',
        'D':'DIVORCED',
        'U':'UNMARRIED'
    }
    
    try:
        return dict_status[input_]

    except (ValueError, KeyError):
        return ('The initial is not recognized')

def main():
    ''' A function that holds the main Program '''
    input_= input('Choose Your Marital status from the given options (S/M/D/U): ').upper()
    print()
    print(f'Your Marital Status is : {printStatus(input_)}')
    print()



if __name__ == '__main__':
    main()
    
