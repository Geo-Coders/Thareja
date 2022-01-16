# Write a program to compute F(n,r) where F(n,r) can be 
# recursively defined as
# F(n,r) = F(n-1, r) + F(n-1, r-1)



print('--- Recursive Function Program ---')
print()

def fact(n,r):
    ''' A recursive Function '''
    if n < 2:
        return 1
    return (fact(n-1,r) + fact(n-1,r-1))


def main():
    ''' This function contain the main body of the program '''
    n = int(input("Enter the value of n : "))
    r = int(input("Enter the value of r : "))
    print()
    print(f"F(n,r) = {fact(n,r)}")


if __name__ == '__main__':
    main()