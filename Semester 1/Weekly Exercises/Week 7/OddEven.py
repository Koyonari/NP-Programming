#An Yong Shyan, S10258126B

odd = []
even = []

#Use loops to enter number
number = 1

while number != 0:
    number = int(input('Please enter a number (0 to end): '))
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

even.sort()
even.pop(1)
odd.sort()

#For loop to find average
total = 0

for num in (odd + even):
    total += num

no_of_numbers = len(odd + even)
average = total / no_of_numbers

#Print out odd, even and average
print('Odd numbers: ', odd)
print('Even numbers: ', even)
print('Average = {:.2f}'.format(average))