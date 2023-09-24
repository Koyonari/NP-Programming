#Programming I

#####################################
#            Mission 2.1            #
#    Compound Interest Calculator   #
#####################################

#Background
#==========
#Tom won a lottery amounting to $10000, and he is deciding if he should
#deposit it into a bank account to accumulate interest.

#Tom wishes to find out how much he will have in the bank account after
#a specified number of years, given his input.

#Requirements
#============
#1) Write pseudocode that sets the principal amount of $10000 to variable p,
#   annual nominal interest rate of 8% to variable r, number of times the
#   interest is compounded per year of 12 to variable n. The number of years
#   that the money will be compounded, t, is given by the user. Calculate
#   and print the final amount (up to 3 decimal places) after t years.
#   Note: Refer to the question in Coursemology for the formula.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - P (principal amount)
#   - r (annual nominal interest rate [as a decimal])
#   - n (number of times the interest is compounded per year)
#   - t (number of years)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#1. Prompt user for principal amount, assigning it to the variable, P
#2. Prompt user for annual nominal interest rate in float, assigning it to the variable, r
#3. Prompt user for number of times the interest is compounded per year, assigning it to the variable, n
#4. Prompt user for number of years, assigning it the variable , t
#5. Calculate using the P * (1 + r / n) ** (n * t), assigning it to the variable, a
#6. Convert a to 3 decimal places, assigning it to the variable, A
#7. Print the final amount after t years which is A

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
'''Prompt user for Principal, annual nominal interest rate,
number of times the interest is compounded per year and number
of years '''
P = float(input('Enter Principal amount: $'))
r = float(input('Enter annual nominal interest rate in decimal: '))
n = float(input('Enter number of times the interest is compounded per year: '))
t = float(input('Enter number of years: '))

#Process
#Calculate Final amount
a = P * (1 + r / n) ** (n * t)
A = round(a, 3)

#Output
#Print final amount
print('Final amount after t years: $' + str(A))