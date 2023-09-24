#An Yong Shyan (S10258126B) - IT03

#Question 1 Part A

#Read data and store in a nested list
trip_prices_list = []

f = open('trip_prices.txt', 'r')

#Remove whitespace and split
for line in f:
    line = line.strip().split(',')
    trip_prices_list.append(line)
#Exclude the first line
trip_prices_list = trip_prices_list[1:]
print('Trip prices:\n' + str(trip_prices_list))

#Question 1 Part B

#import math
import math

#Prompt user for number of children and adults
adults = int(input('Number of adults: '))
children = int(input('Number of children: '))
extension = int(input('Number of extension: '))

#Calculate and print the number of adult twin package
print('Number of adult-twin for the tour package / land tour:', math.floor(adults/2))

#Calculate and print the number of adult-single
print('Number of adult-single for the tour package / land tour:', (adults % 2))

#Calculate and print the number of children
print('Number of children for the tour package / land tour:', children)

#Calculate and print the number of rooms for extension
if type((adults + children)/2) == float:
    room = math.floor((adults + children)/2) + 1
else:
    room = (adults + children)/2
print('Number of rooms for extension per night:', room)

#Question 1 Part C
total_amount = []
amount_land = []

for x in trip_prices_list:
    total = x[1:]
    for y in total:
        total_y = sum(total)

total_amt_list = zip(total_amount, amount_land)

for i in trip_prices_list:
    '{:6} {:6} {:6} {:6} {:6} {:11} {:11} {:11} {:15} {:15}'.format(trip_prices_list[:-1], *total_amt_list)
        


#Question 1 Part D
total_amt_list = [[15240, 22460], [17740, 25460], [20440, 29660]]
print('Options Available for SGD$25000 budget:')
for t, q in enumerate(total_amt_list):
    for i, w in enumerate(q):
        if w < 25000 and t == 0 and i == 0:
            print('\tHotel A w/o land tour')
        elif w < 25000 and t == 1 and i == 0:
            print('\tHotel B w/o land tour')
        elif w < 25000 and t == 0 and i == 1:
            print('\tHotel A w land tour')
        elif w < 25000 and t == 1 and i == 1:
            print('\tHotel B w land tour')
        elif w < 25000 and t == 2 and i == 0:
            print('\tHotel C w/o land tour')
        elif w < 25000 and t == 2 and i == 1:
            print('\tHotel C w land tour')
            
