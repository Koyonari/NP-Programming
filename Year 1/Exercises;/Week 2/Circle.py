import math

#Prompt user for a and b
a = float(input('Enter the length of a: '))
b = float(input('Enter the length of b: '))

c = (math.sqrt(a**2 + b**2))
area = math.pi * (c / 2) ** 2
print('The length of c is ' + str(c))
print('The area of the circle is ' + str(area))