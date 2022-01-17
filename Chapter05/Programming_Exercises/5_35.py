# Write a function that accepts three integers, and returns True if
# they are sorted, otherwise it returns False.

print('--- A Program that check if entered integers are sorted---')
print()

def is_sorted(args):
    ''' A function that check if arguments are sorted '''
    if args == sorted(args): 
        return True
    else:
        return False
 
arg_list= []
for i in range(1,4):
    args_= (input(f'Enter integer {i} to evaluate: '))
    arg_list.append(args_)

temp= is_sorted(arg_list)

#print(sorted(arg_list))

print()

if temp == True:
    print('The Entered digits are sorted')
else:
    print('The entered digits are not sorted')

print()
