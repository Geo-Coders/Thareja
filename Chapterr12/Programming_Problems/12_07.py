# Write a program that has multiple except blocks.

print('--- A Program with Multiple Except Blocks ---')
print()

try:
    print('1' + 1)
    print(sum)
    print(1/0)

except NameError:
    print("sum does not exist")

except ZeroDivisionError:
    print("Cannot divide by 0")

except:
    print("Something went wrong")

print()