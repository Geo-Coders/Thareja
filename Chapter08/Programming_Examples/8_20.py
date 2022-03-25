# Write a program to generate in the Fibonacci sequence and store it in a list
# Then find the sum of the even- valued terms

a = 0
b = 1
n = int(input('Enter the number of terms : '))
i = 2
List = [a,b]
while i<n:
    s = a + b
    List.append(s)
    a = b
    b = s
    i += 1
print(List)
i = 0
sum = 0
while i<n:
    sum += List[i]
    i += 2 
print(f'SUM = {sum}')