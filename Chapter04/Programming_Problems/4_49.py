# A video library rents new videos for $ 75 a day, and old movies for $ 50 a day.
# Write a program to calculate the total charge for a customer's video rentals.
# The Program should prompt the usedr for the number of each type of video and output the total cost.

print('\t\t--- Video Rentals Program ---')
print()

new_videos= int(input('Enter the number of new videos rented in a day: '))
old_videos= int(input('Enter the number of old videos rented in a day: '))

new_video_totalcost= new_videos * 75
old_videos_totalcost= old_videos * 50

print()

print(f'The total cost collected on New videos is {new_video_totalcost}')
print(f'The total cost collected on Old videos is {old_videos_totalcost}')

print()

print(f'The total cost : {new_video_totalcost + old_videos_totalcost}')


