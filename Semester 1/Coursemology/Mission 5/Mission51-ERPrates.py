#Programming I

##########################################
#              Mission 5.1               #
#   ERP Rates at Orchard Cordon gantry   #
##########################################

#Background
#==========
#Any cars entering Orchard Road from Scotts Road from Monday to Friday will
#have to pay the following ERP charges depending on the time of entry.


########################################
#      Time               #  ERP Rate  #
########################################
#  Before 12.00           #    Free    #
#  12.00 <= time < 17.30  #    0.50    #
#  17.30 <= time < 17.35  #    1.00    #
#  17.35 <= time < 18.00  #    1.50    #
#  18.00 <= time < 18.55  #    2.00    #    
#  18.55 <= time < 19.00  #    1.50    #
#  19.00 <= time < 19.55  #    1.00    #
#  19.55 <= time < 20.00  #    0.50    #
#  20.00 or after         #    Free    #
########################################


#Write a Python program to check how much the ERP rate is and to deduct this
#amount from the cash card and display its new value.

#The program is to prompt user for the current value in the cash card and the
#time of entry into Orchard Road. Pass these values into the function, which
#determines the erp rate. If there's erp charges, checks whether the card has
#sufficient balance, deducts the charges from the card if there's sufficient
#balance. Sets the deduction status. Returns the erp rate, card value and
#deduction status as a list. Display the results return from the function with
#appropriate messages.
#You may use float value for the time of entry and assume that the value is
#always valid. 

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - time_of_entry
#   - card_value
#   - erp_rate
#   - successful_deduction


#START CODING FROM HERE
#======================


#Determine the ERP rate, calculate New Value in Cash Card
#return a list containing the new value in card and whether deduction is successful 
def calculate_card_value(card_value, time_of_entry):

    #Check ERP rate using if..elif..else
    if time_of_entry < 12.00 or time_of_entry >= 20.00:
        erp_rate = 0
    elif 12.00 <= time_of_entry < 17.30:
        erp_rate = 0.50
    elif 17.30 <= time_of_entry < 17.35:
        erp_rate = 1.00
    elif 17.35 <= time_of_entry < 18.00:
        erp_rate = 1.50
    elif 18.00 <= time_of_entry < 18.55:
        erp_rate = 2.00
    elif 18.55 <= time_of_entry < 19.00:
        erp_rate = 1.50
    elif 19.00 <= time_of_entry < 19.55:
        erp_rate = 1.00
    elif 19.55 <= time_of_entry < 20.00:
        erp_rate = 0.50
        
    print('The ERP rate is ${:.2f}'.format(erp_rate)) #Modify to display ERP Rate
    if erp_rate > 0:  #Check if there's erp charges
        if card_value - erp_rate >= 0:  #Check if there is enough balance to pay ERP charge
            card_value = card_value - erp_rate #Modify to calculate new value in cash card
            successful_deduction = True  #Set the value for successful_deduction
        else:
            print('You do not have enough balance in your card to pay for the ERP charge.')  #Modify to display insufficent balance in cash card
            print('The amount is not deducted, you need to pay a fine for this.')
            successful_deduction = False  #Set the value for successful_deduction
    else:  #if there's no erp charges
        successful_deduction = False   #Set the value for successful_deduction
        
    return [erp_rate, card_value, successful_deduction]  #Do not remove this line

#Prompt user for current value in cash card and time of entry
card_value = float(input('Please enter the current value in cash card: $'))
time_of_entry = float(input('Please enter time of entry at ERP gantry: '))

#Do not remove the next line that calls the function
result = calculate_card_value(card_value, time_of_entry)

#Print result from function call if there's erp charges
if result[2] == True:
    print('The amount is deducted successfully.')

#Print final card value
print('Your card value is ${:.2f}'.format(result[1])) #Modify to display final card value

#input 50,18.30 output [2.0, 48.00, True]
#input 30,20.00 output [0, 30.00, False]
#input 0.50,17.32 output [1.0, 0.50, False]