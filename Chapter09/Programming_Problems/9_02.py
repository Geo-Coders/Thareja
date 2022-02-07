# Write a program that has class Cars.
# Create two objects and set car1 to be a red convertible with price $ 10 and name Pugo
# and car2 to be a blue sedan named avo worth $6

class Cars:
    def __init__(self, name, type, color, price):
        self.name = name
        self.type = type
        self.color = color
        self.price = price
    def display(self):
        print(f'Name : {self.name}, Type : {self.type}, Color : {self.color}, Price : {self.price}')

car1 = Cars('Pugo', 'Convertible', 'Red', 10)
car2 = Cars('Avo', 'Sedan', 'Blue', 6)
    
car1.display()
car2.display()