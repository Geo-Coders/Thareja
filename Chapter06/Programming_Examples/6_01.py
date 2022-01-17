# Write a program to print the following pattern.

for i in range(1,7):
    ch= 'A'
    print()
    for _ in range(1, i+1):
        print(ch, end=' ')
        ch= chr(ord(ch) + 1)