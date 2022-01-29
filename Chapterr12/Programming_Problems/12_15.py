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
enter_delta = datetime.timedelta(hours=enter.hour, minutes=enter.minute, seconds=enter.second)
exit_delta = datetime.timedelta(hours=exit.hour, minutes=exit.minute, seconds=exit.second)
difference_delta = exit_delta - enter_delta

print('--- A Program to display duration of an online test---')
print()

class Time:
    def __init__(self):
        try:
            self.start= time.strptime(input('self.start the starting time (eg HH:MM:SS) : '), '%H:%M:%S')
            self.end= time.strptime(input('self.start the ending time (eg HH:MM:SS) : '), '%H:%M:%S')

        except ValueError:
            print('Time data self.started does not match format \'%H:%M:%S\'')

    def checking_times_duration(self):
        if self.end_time < self.start_time:
            raise InvalidEndingTime
        else:
            self.start_delta = datetime.timedelta(hours=self.start.hour, minutes=self.start.minute, seconds=self.start.second)
            self.end_time_delta = datetime.timedelta(hours=self.end_time.hour, minutes=self.end_time.minute, seconds=self.end_time.second)
            difference_delta = self.end_time_delta - self.start_delta
            print(f'Time left : {difference_delta}')

    def show(self):
        print(f'Ending time : {self.end_time}')
        print(f'Starting time : {self.start_time}')

test= Time()
test.checking_times_duration()