#An Yong Shyan (S10258126) - IT03

#Prompt user for x and y
y = int(input('Please enter the number of books that are late: '))
x = int(input('Please enter the number of days the books are late: '))

#If statements for prices
if y == 1 and x ==1:
    fine = 1.2
elif y == 1 and x > 1:
    fine = (2**(x-1)) * 0.3 + 1
elif y > 1 and x ==1:
    fine = 0.15 * y + 1.2
elif x > 1 and y > 1:
    fine = (2**x) * 0.15 * y + 1.2

print('The fine for', y, 'book(s) for', x, 'day(s) is ${:.2f}'.format(fine))
