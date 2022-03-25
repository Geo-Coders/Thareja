# Write a program that has a list of numbers
#(both positive as well as negative) Make a new tuple that has only positive vallues from this list

Tup = (-10,1,-2,-9,3,4,-8,5,6)
newTup = ()
for i in Tup:
    if i > 0:
        newTup +=(i,)
print(newTup)