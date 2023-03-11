# A program that re-raises an exception

print('--- A Program to re-raise an exception---')
print()
try:
    raise NameError
except:
    print('Re-raising exception')

