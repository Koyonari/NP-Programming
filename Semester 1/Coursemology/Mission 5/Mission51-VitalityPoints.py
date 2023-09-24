#Programming I

#######################
#     Mission 5.1     #
#   Vitality Points   #
#######################

#Background
#==========
#To encourage their customers to exercise more, insurance companies are giving
#vouchers for the distances that customers had clocked in a week as follows:


######################################################
#     Distance (km)     #  Gift                      #
######################################################
#  Less than 25         #  eSticker                  #
#  25 <= distance < 50  #  $5 Cold Storage eVoucher  #
#  50 <= distance < 75  #  $10 Starbuck eVoucher     #
#  More than 75         #  $20 Subway eVoucher       #
######################################################


#Write a Python program to check and display the gift that customer will recieve.

#The program is to prompt user for the total distance he had travelled (by walking
#or running) in a week and check which gift he will get and display the information
#to him.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - distance
#   - gift

#START CODING FROM HERE
#======================


#Check gifts to be given to customer
def check_gift(distance):

    if distance < 25:
        gift, value = 'eSticker', 0  #Check gift and value to be given
        
    elif 25 <= distance < 50:
        gift, value = '$5 Cold Storage eVoucher', 5 #Check gift and value to be given
    
    elif 50 <= distance < 75:
        gift, value = '$10 Starbuck eVoucher', 10  #Check gift and value to be given

    else:
        gift, value = '$20 Subway eVoucher', 20  #Check gift and value to be given
        
    print('You will receive a', gift) #Modify to display gift to be given

    return value  #Modify to return the value of gift


#Prompt user for the total distances travelled (either by walking or running).
distance = int(input("Enter total distance travelled in a week (in kilometres): "))

#Do not remove the next line
value = check_gift(distance)

print('The value of your gift is', value)#Modify to print value received

#Input: 10  output: 2
#Input: 76  output: 20