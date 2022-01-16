# Write a program to print the Fibonacci series using recursion.

print('--- Fibonacci Series ---')
print()

def fib(n):
    ''' A Fibonacci Series Function '''
    if n <2: 
        return 1
    return (fib(n-1) + fib(n-2))

def main():
    ''' A function that contain the main body of the program '''
    num_= int(input('Enter the number of terms: '))
    for i in range(num_):
        print(f'Fibonacci {i} = {fib(i)}')


if __name__ == '__main__':
    main()