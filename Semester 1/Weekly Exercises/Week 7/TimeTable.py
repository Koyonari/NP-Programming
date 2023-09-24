#An Yong Shyan, S10258126B

#Prompt user to enter the number
num = int(input('Please enter the number: '))

#For loop to print out time table
multiple = 0
for i in range(10):
    multiple += 1
    if multiple < 10:
        print(' ', num, 'x', multiple, ' =', num*multiple)
    else:
        print(' ', num, 'x', multiple, '=', num*multiple)

print('The End')