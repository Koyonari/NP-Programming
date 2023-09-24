#Programming I

##################################
#           Mission 4.1          #
#   Driving License Eligiblity   #
##################################

#Background
#==========
#In Singapore to apply for a driving license, one must be at least 18 years old

#Write a Python program that prompts user for his age and check whether
#he is eligible to apply for a driving test, display his eligibility.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - age


#START CODING FROM HERE
#======================


#Function to receive age and check whether the person is eligible to apply
#for driving test. Returns the boolean True if the person is eligible.
def check_eligibility(age):

    if age >= 18:  #Check if user is eligible to apply to take a driving test
        print('User is allowed to take a driving test.') #Modify to display that user can apply to take a driving test
        return True #Return True if user is eligible


#Prompt and accept data from user
age = int(input('Enter your age: '))
#Do not remove the next line that calls the function
eligible = check_eligibility(age)

#Print result returned from function
print('Result returned from function is', eligible)

#input 25 output True
#input 17 (no output)