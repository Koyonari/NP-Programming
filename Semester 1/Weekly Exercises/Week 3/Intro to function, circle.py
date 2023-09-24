# An Yong Shyan, 10258126B

import math

#Prompt user for a and b
a = float(input('Enter the length of a: '))
b = float(input('Enter the length of b: '))

#Define function
def calculate_circle(a, b):
    c = (math.sqrt(a**2 + b**2))
    area = math.pi * (c / 2) ** 2
    return area

#Call function, area
print('The area of the circle is ' + str(calculate_circle(a, b)))