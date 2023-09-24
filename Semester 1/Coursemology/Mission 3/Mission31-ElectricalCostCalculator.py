#Programming I

#####################################
#      Mission 3.1                  #
#     Electrical Cost Calculator    #
#####################################

#Background
#==========
#Write a program that prompts user to enter the electricity cost for 3 months
#in a line, separated by ';' and displays the average electricity cost in
#2 decimal places.


#Important Notes
#===============
#1) You are required to include a function called calculate_average(), which
#   accepts a string containing the electricity cost for 3 months separated
#   by ';', calculates and returns the average cost
#2) When testing the program in IDLE, you should prompt the user for the input
#   value. However, you must comment out the input prompt before submitting it
#   in coursemology


#START CODING FROM HERE
#======================

#Define the function, calculate_average()
def calculate_average(mthly_cost):
    #Parse the string, extract the electrical cost, and add to the total
    #Hint:
    # You may either use a combination of the find() built-in string method 
    # and index to extract each month's cost, then total them up
    # or use the split() function to split the string into a list to extract
    # each month's cost, then total them up



    return average #Do not edit/remove this line

#Prompt for input of electrical costs and store in mthly_cost. You must remove this
#statement when submitting in Coursemology


#Do not edit/remove the next line that calls the function to get the average
average = calculate_average(mthly_cost)

#Modify the statement to display the average cost
print(  ) 
