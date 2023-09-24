#Programming I

#########################
#      Mission 4.1      #
#   Passport Validity   #
#########################

#Background
#==========
#All countries around the world require a valid passport for entry and insist
#on travellers having a minimum of six months left on their passport for entry.

#Write a Python program to check whether a person's passport is valid for entry.
#
#The program is to prompt user for the number of months left before his passport
#expires and also the number of months to his intended travel date.
#Display whether he needs to renew his passport.

#Return the Boolean value True if renewal is required, False if not required.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - months_left: stores the number of months left before passport expires
#   - months_to_entry: stores the number of months to travel date


#START CODING FROM HERE
#======================


#Check Validity
def check_validity(months_left, months_to_entry):

    if months_left - months_to_entry > 6:  #Check if user's passport is valid for entry 
        print("Your passport is valid for entry!") #Modify to display that user's passport is valid for entry
        return False #Modify accordingly
    else:
        print('You need to renew your passport.') #Modify to display that user needs to renew his passport
        return True #Modify accordingly


#Prompt and accept data from user.
months_left = int(input('Enter number of months left before passport expires: '))
months_to_entry = int(input('Enter number of months to travel date: '))
    
#Do not remove the next line that calls the function
validity = check_validity(months_left, months_to_entry)
print(validity) #Modify to print the result returned from function

#input 50,9 output False
#input 12,9 output True