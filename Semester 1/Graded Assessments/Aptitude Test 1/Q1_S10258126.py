#An Yong Shyan (S10258126) - IT03

import math

#Prompt user for radius and height of cylinder
h = float(input('Enter height of cylinder in cm: '))
r = float(input('Enter radius of base circle of cylinder in cm: '))

#Calculate total surface area
sa = 2 * math.pi * r**2 + 2 * math.pi * r * h
dp_sa = '{:.2f}'.format(sa)

#Print out total surface area
print('Total Surface Area is: ' + str(dp_sa) + 'cm squared')
