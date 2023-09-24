#Programming I

#####################################
#            Mission 2.2            #
#           Saving Calculator       #
#####################################

#Background
#==========
#Tom remembers the compound interest calculator that he did in Mission 1.
#Instead of calculating the compound interest of a given principal sum after
#x number of years, he would like to calculate the number of years needed to
#reach a certain final amount with an initial savings at a fixed interest rate.
#You may refer to the question in Coursemology for the formula

#Requirements
#============
#Write a Python program to get the input for the final amount and initial saving,
#calculate the number of years needed to reach the final amount. Assume that
#the annual interest rate is 5% and the interest is compounded monthly.
#Display the result as a smallest integer number that is just bigger than the
#result calculated. E.g. print 6, if it is bigger than 5 but less than 6.

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Do you need to import any module?
import math

#Input
#Prompt user for a which is final amount and initial saving
a = float(input('Enter final amount: $'))
initial_saving = float(input('Enter initial saving: $'))
p = float(input('Enter Principal Amount: $'))
r = 5
n = 12

#Process
#Calculate no. of years when r = 5 and n = 12
t = (math.log(a/p)) / (n * math.log( 1 + r / n))

#Output
print('It will take' , math.ceil(t) , 'years.')
