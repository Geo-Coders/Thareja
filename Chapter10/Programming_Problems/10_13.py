# Write a program for a publishing company that markets both printed books and audio-visual lectures
# stored on CDs. Write a class Publication that stores title and price.
# Derive a class book which has an additional member as no_pages and a class Lecture with member play_time.

print('--- A Program for Publishing Company ---')
print()

class publish:
    def __init__(self):
        self.title=input("Enter the title: ")
        self.price=int(input("Enter the price : "))

class book(publish):
    def __init__(self):
        super().__init__()
        self.no_of_pages=int(input("Enter the number of pages: "))

    def display(self):
        print(f'{self.title} of {self.no_of_pages} Pages and Price Rs. {self.price}')
        print()

class audio_visual(publish):
    def __init__(self):
        super().__init__()
        self.play_time=int(input("Enter the playtime in hours: "))

    def display(self):
        print(f'{self.title} of Play time {self.play_time} Hours and Price Rs. {self.price}')
        print()

b1=book()
b1.display()
a1=audio_visual()
a1.display()