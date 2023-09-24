#An Yong Shyan, S10258126B

#Prompt user for target pushups
target = int(input('Enter target number of pushups: '))

#Use a while loop 
day = 0
total = 0

while total < target:
    day += 1
    pushups = int(input('Day {}: How many pushups did you do today? '.format(day)))
    total += pushups

#Print out total pushups
print('You did a total of {} pushups.'.format(total))
print('You hit your target in {} days!'.format(day))