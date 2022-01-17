# Write a program to calculate electricity bill based on following information
# units     Rate of charge
# 0-150     $3 per unit
# 151-300   $100 plus $3.75 per unit exceeding 150 units
# 301-450   $250 plus $4 per unit exceeding 350 units
# 451-600   $300 plus $4.25 per unit exceeding 450 units
# Above 600 $400 plus $5 per unit exceeding 600 units

units = int(input('Enter the number of units used : '))

if units > 0 and units <= 150:
    charges = units * 3
elif units > 150 and units <= 300:
    charges = 100 + 3.75 * (units- 150)
elif units > 300 and units <= 450:
    charges = 250 + 4 * (units - 350)
elif units > 450 and units <= 600:
    charges = 300 + 4.25 * (units - 450)
else:
    charges = 400 + 5 * (units - 600)
print(f'Your charges are {charges}')