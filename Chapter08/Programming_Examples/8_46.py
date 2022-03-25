# Write a program that prompts the user to enter a file name.
# Open the file and print the frequency of each word in it

filename = input('Enter the file name : ')
file = open(filename)
counts = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)