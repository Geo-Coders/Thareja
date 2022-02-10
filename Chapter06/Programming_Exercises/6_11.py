# Write a program to change a given string to a new string where the first and last characters
# have been exchanged.

print('--- A Program to Remove character with Odd Index ---')
print()

def change_string(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_string('abcd'))
print(change_string('12345'))

print()

