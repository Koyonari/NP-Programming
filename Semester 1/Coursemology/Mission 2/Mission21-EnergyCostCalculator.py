#Programming I

###############################
#       Mission 2.1           #
#    Energy Cost Calculator   #
###############################

#Background
#==========
#Ever wonder the energy cost of running an appliance or electronic device?
#Here is a simple calculation to get that figure.

#Step 1:
#Monthly electricity consumption =
#   (Power rating [Watts] of device * Number of hours used per day)/1000

#Step 2:
#Cost = Monthly electricity consumption * Electricity tariff
#                                         ($0.2743 as of April 2023 for SP group)

#Laptop computers may peak at a maximum draw of only 60 watts,
#whereas common desktops may peak around 175 watts.

#Requirements
#============
#1) Write pseudocode for the Energy Cost Calculator.
#   The solution should prompt user for the power rating of a device and the
#   number of hours used per day. After which, display the calculated cost in
#   4 decimal places.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - power_rating
#   - hours

#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#1. Prompt user for power rating in watts, assigning to the variable, power_rating
#2. Prompt user for number of hours used per day, assigning to the variable, hrs
#3. Calculate montly electricity consumption, assigning to the variable, elec_con
#4. Calculate cost in $, assigning to the variable, cost
#5. Convert cost to 4 decimal places, assigning to the variable, final_cost
#6. Print final_cost

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
#Prompt user for power_rating and hrs
power_rating = int(input('Power rating in Watts: '))
hours = float(input('Number of hours used per day: '))

#Process
#Calculate montly electricity consumption and cost
elec_con = power_rating * hours / 1000
cost = elec_con * 0.2743

#Convert to 4 d.p.
final_cost = round(cost, 4)

#Output
print('Final Cost: $' + str(final_cost))

