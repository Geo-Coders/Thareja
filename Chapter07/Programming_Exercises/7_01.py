# Write a program that reads text from a file and writes it into another file but in the reverse order

print('--- A Program to Reverse texts ---')
print()

file = "<path to file>"
with open(file) as f:
    lines = f.readlines()

reverse_file = "e:\\python\\reversed.txt"
with open(reverse_file, 'w') as rev:
    rev.writelines(lines[::-1])