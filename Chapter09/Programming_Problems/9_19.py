# Write a program that uses a time structure within a class. 
# Enter any time and your favorite show's time.
# The Program must display how much time is left for it to start.

print('--- A Program to display time of my favorite show ---')
print()

import datetime
class ShowTime:
    def __init__(self):
        self.show_time = datetime.datetime.strptime(
            input('Enter the show time(HH:MM:SS) : ') , 
            '%H:%M:%S').time()

    def time_to_show(self):  
        show_time_today = datetime.datetime.combine(
            datetime.date.today(),
            self.show_time
        )      
        time_left = show_time_today - datetime.datetime.now()
        
        print('Time left : ', time_left)

s = ShowTime()
s.time_to_show()