#Programming I

#####################################
#            Mission 2.2            #
#           Cone Calculator         #
#####################################

#Background
#==========
#Tom has learnt that if he knows the radius of the base circle and height
#of a right circular cone, he is able to calculate the volume and the surface
#area of the cone (refer to the question in Coursemology for the formulae)

#Requirements
#============
#Write a Python program to calculate the volume and surface area (including
#the base circle) of a right circular cone whose base circle radius and heeight
#are entered by the user. Display the results in a nicely formatted string,
#like the following:
#    For a cone with base circle radius 3.0 and height 4.0:
#    Slant height is 5.00
#    Volume is 37.6991
#    Surface area (including base circle) is 75.3982
#Note: values shown above are just examples

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Do you need to import any module?
import math

#Input
#Prompt user for radius and height of cone
r = float(input('Enter radius of cone: '))
h = float(input('Enter height of cone: '))

#Process
#Caculate slant height, volume and surface area
s = math.sqrt(r**2 + h**2)
v = 1/3 * (math.pi * r**2 * h)
a = math.pi * r**2 + math.pi * r * s

#Output
#Print out slant height, volume and surface area
print('For a cone with base circle radius', r , 'and height', h)
print('Slant height is' , '{:.2f}'.format(s))
print('Volume is', '{:.4f}'.format(v))
print('Surface area (including base circle) is' , '{:.4f}'.format(a))