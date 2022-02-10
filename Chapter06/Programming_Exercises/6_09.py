# Write a program to remove the nth index character 
# from a non-empty string.

print('--- A Program to Remove the nth index character from a non-empty string ---')
print()

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
      
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

