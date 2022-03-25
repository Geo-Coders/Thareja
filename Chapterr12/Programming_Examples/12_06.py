# Write a program that prints the first 30 numbers.
# Each number should be printed after a fixed short interval of time
# Make use of a timer which prints each number when the timer goes off and exception is generated

class TimeUp(Exception):
    pass
def message(c):
    start_timer = 0
    stop_timer = 10000
    count = start_timer
    try:
        while True:
            count += 1
            if count == stop_timer:
                raise TimeUp
    except TimeUp as t:
        print(c, end = ' ')
for i in range(31):
    message(i)