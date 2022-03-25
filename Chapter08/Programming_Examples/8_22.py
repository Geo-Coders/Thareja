# Write a program to find the median of a list of numbers

List = []
n = int(input('Enter the number of elements to be inserted in the list : '))
for i in range(n):
    print(f'Enter number {1+1} : ')
    num = int(input())
    List.append(num)
print('Sorted List is........')
List = sorted(List)
print(List)
i = len(List) - 1
if n % 2 !=0:
    print(f'MEDIAN = {List[i//2]}')
else:
    print(f'MEDIAN = {(List[i//2] + List[i + 1//2])/ 2}')