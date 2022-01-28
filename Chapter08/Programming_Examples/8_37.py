# Write a program that creates two dictionaries. One that stores coversion
# values from meters to centimeters and the other that stores values from 
# centimeters to meters.

m_cm= {x: x*100 for x in range(1,11)}
temp= m_cm.values()
cm_m= {x: x/100 for x in temp}

print(f'Meters : Centimeters {m_cm}')
print(f'Centimeters : Meters {cm_m}')