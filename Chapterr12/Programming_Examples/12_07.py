# Write a program which infinitely prints natural numbers. Raise the StopIteration exception
# after displaying first 20 numbers to exit from the program

def display(n):
    while True:
        try:
            n += 1
            if n == 21:
                raise StopIteration

        except StopIteration:
            break

        else:
            print(f'{n}', end=" ")

i = 0
display(i)