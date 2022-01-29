# Write a program that validates user's input.

print('--- A program to valid user\'s input ---')
print()

class InvalidAge(Exception):
    def display(self):
        print('Invalid Age entered...!')

class InvalidName(Exception):
    def display(self):
        print('Invalid Name entered...!')

class InvalidCountry(Exception):
    def display(self):
        print('Invalid Country entered...!')

class InvalidTribe(Exception):
    def display(self):
        print('Invalid Tribe entered...!')

try:
    name = input('Enter Your name : ')
    if len(name) == 0:
        raise InvalidName

    age = int(input('Enter Your Age : '))
    if age < 18:
        raise InvalidAge

    country = input('Enter Your Country : ')
    if country not in ['Tanzania', 'Kenya', 'Uganda', 'Rwanda', 'Ethiopia']:
        raise InvalidCountry

    tribe = input('Enter Your Tribe : ')
    if tribe not in ['Al-Famawiy']:
        raise InvalidTribe

except InvalidName as n:
    n.display()

except InvalidCountry as c:
    c.display()

except InvalidTribe as t:
    t.display()

except InvalidAge as a:
    a.display()

else:
    print(f"""
    Your Details are :-
    \t1. Name : '{name}
    \t2. Country : {country}
    \t3. Tribe : {tribe}
    \t4. Age : {age}
    """)

print()