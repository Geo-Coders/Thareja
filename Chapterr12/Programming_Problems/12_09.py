# Write a Program with except: handler

print('--- A Program with except: handler ---')
print()

while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    
    except ValueError:
        print("No valid integer! Please try again ...")

print("Great, you successfully entered an integer!")

