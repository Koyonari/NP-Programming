#Programming I

#####################################
#            Mission 2.1            #
#           Coin Converter          #
#####################################

#Background
#==========
#Tom has 2 50-cent coins, 4 20-cent coins, 6 10-cent coins and 9 5-cent coins.
#He would like calculate the total amount in dollars.

#Requirements
#============
#Develop a pseudocode and Python program to solve the following problem:
#   -Given a number of 50-cent coins, 20-cent coins, 10-cent coins
#    and 5-cent coins, calculate the amount in dollars, print the
#    output with proper description and the amount in proper format

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of your program.
#2) You MUST (at least) use the following variables:
#   - cent50 (number of 50-cent coins)
#   - cent20 (number of 20-cent coins)
#   - cent10 (number of 10-cent coins)
#   - cent5  (number of 5-cent coins)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#1. Prompt user for number of 50-cent coins, assigning it to the variable, cent50
#2. Prompt user for number of 20-cent coins, assigning it to the variable, cent20
#3. Prompt user for number of 10-cent coins, assigning it to the variable, cent10
#4. Prompt user for number of 5-cent coins, assigning it to the variable, cent5
#5. Calculate value of 50-cent coins, assigning it to the variable, value50
#6. Calculate value of 20-cent coins, assigning it to the variable, value20
#7. Calculate value of 10-cent coins, assigning it to the variable, value10
#8. Calculate value of 5-cent coins, assigning it to the variable, value5
#9. Calculate total value, assigning it to the variable, total
#10. Convert total to 2 decimal places, assigning it to the variable, total_value
#11. Print total value

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
#Prompt user for number of coins
cent50 = int(input('Number of 50-cent coins: '))
cent20 = int(input('Number of 20-cent coins: '))
cent10 = int(input('Number of 10-cent coins: '))
cent5 = int(input('Number of 5-cent coins: '))

#Process
#Calculate value of coins 
value50 = cent50 * 0.5
value20 = cent20 * 0.2
value10 = cent10 * 0.1
value5 = cent5 * 0.05

total = value50 + value20 + value10 + value5

#Convert to 2 d.p.
total_value = round(total, 2)

#Output
print('Total amount in dollars: ' + str(total_value))
