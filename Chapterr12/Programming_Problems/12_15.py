# write a program that has a class TIME. self.start the time when a
# user started an online test and completed the test. Subtract the two
# time values and dispaly the duration in which the test was completed.
# Throw exceptions whenever need arises (like invalid data, or if start time
# is greater than completion time.)

import datetime
import time


class InvalidEndingTime(Exception):
    def display(self):
        print('Invalid Age self.started...! starting time can never be greater than the ending time')


enter = datetime.time(hour=1)  # Example enter time
exit = datetime.time(hour=2)  # Example start time
enter_delta = datetime.timedelta(
    hours=enter.hour, minutes=enter.minute, seconds=enter.second)
exit_delta = datetime.timedelta(
    hours=exit.hour, minutes=exit.minute, seconds=exit.second)
difference_delta = exit_delta - enter_delta

print('--- A Program to display duration of an online test---')
print()


class Time:
    def __init__(self):
        try:
            self.in_hrs = int(input("Enter the time of entrance (HH) : "))
            self.in_min = int(input("Enter the time of entrance (MM) : "))
            self.out_hrs = int(input("Enter the time of Leaving (HH) : "))
            self.out_min = int(input("Enter the time of leaving (MM) : "))

        except ValueError:
            print('Invalid Time data')

    def checking_times_duration(self):
        end_time = self.out_hrs + (self.out_min/60)
        start_time = self.in_hrs + (self.in_min/60)
        if end_time < start_time:
            raise InvalidEndingTime
        else:
            time_spent = (end_time) - (start_time)
            print(f'Time left : {time_spent} Hours')

    def show(self):
        print(f'Ending time : {self.out_hrs}:{self.out_min}')
        print(f'Starting time : {self.in_hrs}:{self.in_min}')


test = Time()
test.checking_times_duration()
