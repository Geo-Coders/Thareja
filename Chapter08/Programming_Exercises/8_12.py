# Write a program that has a dictionary of your friends name(as keys) and their birthdays
# Print the items in the dictionary in a sorted order
# Prompt the user to enter a name and check if it is present in the dictionary
# If it does not exist, then ask the user to enter DOB. Add the details in the dictionary

print('----- A Dictionary of birthdays-----')
print()

def main():
    friends = {'Caroline' :23/1/2000, 'Joy' : 25/12/2000, 'Faith' : 11/4/2000, 'Juliet' : 5/5/2000}
    print(sorted(friends.keys()))
    check = input('Enter the name you want to check in the dictionary : ')
    result = friends[check] if check in friends else None
    if result == None:
        print('No data')
    
    else:
        print('is in the dictionary list')
        
        
if __name__ == "__main__":
    main()
    
    