import random 

#Generate 2 integers
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

#Prompt user for sum of 2 integers
sum = int(input('Enter the sum of ' + str(num1) + ' and ' + str(num2) + ': '))

#Check if user input is correct
if sum == num1 + num2:
    print('Your answer is correct!')
else:
    print('Your answer is wrong.')
    print('The correct answer is', str(num1 + num2) + '.')