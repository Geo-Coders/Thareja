# Write a program to convert time into minutes

def convert_time_in_min(hrs, minute):
    minute = hrs * 60 +minute
    return minute
h = int(input('Enter the hours : '))
m = int(input('Enter the minutes : '))
m = convert_time_in_min(h,m)
print(f'Minutes = {m}')