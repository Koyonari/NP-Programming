#Programming I

#####################################
#            Mission 2.2            #
#           Triangle Calculator     #
#####################################

#Background
#==========
#Tom has learnt that if he knows the length of the 3 sides of a triangle,
#he is able to calculate the area by using the Heron's formula (please check
#it out in internet if you cannot remember the formula).

#Requirements
#============
#Write a Python program to calculate the perimeter and area of a triangle
#whose length of the 3 sides are entered by the user. Display the results
#in a nicely formatted string, like the following:
#    For a triangle with sides 3.0, 4.0 and 5.0
#    The perimeter is 12.00
#    The area is 6.00
#Note: values shown above are just examples

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Do you need to import any module?
import math

#Input
#Prompt user for a, b and c values
a = float(input('Enter your a value: '))
b = float(input('Enter your b value: '))
c = float(input('Enter your c value: '))

#Process
#Calculate perimeter and area
p = a + b + c
s = (a + b + c) / 2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))
P = '{:.2f}'.format(p)
Area  = '{:.2f}'.format(area)

#Output
#Print out value of sides, perimeter and area
print('For a triangle with sides' , str(a) + ',' , b , 'and' , c)
print('The perimeter is', P)
print('The area is', Area)