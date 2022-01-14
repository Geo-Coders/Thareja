# ----- program 4.16 -----
# Write a program to calculate the sum and average of first 10 numbers
i = 0
s = 0
while i <= 10:
    s = s + i
    i +=1
avg = float(s)/10
print('The sum of first 10 numbers is : ',s)
print('The average of the first 10 numbers is : ', avg)