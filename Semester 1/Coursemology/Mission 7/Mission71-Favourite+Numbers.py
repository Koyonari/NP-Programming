#Programming I

#######################
#     Mission 7.1     #
#  Favourite Numbers  #
#######################

#Background
#==========
#Tom is investigating a suspect and found out that
#the suspect always configure his pin code with
#numbers that are divisible by both 5 and 7. Tom wants
#to find out the list of numbers that are divisible
#by 5 and 7 within a given range. Write a Python program
#that prompts the user to enter 2 integers to indicate
#the start and end of the range (both integers are
#inclusive in the range), and print the list of numbers
#that fulfil the conditions. The following shows a
#sample output of the program.
#
#Enter the starting number:50
#Enter the ending number:150
#Suspect's numbers are: [70, 105, 140]




#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - start_range
#   - end_range
#   - fav_numbers



#START CODING FROM HERE
#======================


#function to find favourite numbers
def find_favourite_numbers(start_range,end_range):
    fav_numbers = []
    for i in range(start_range, end_range):
        if i % 5 == 0 and i % 7 == 0:
            fav_numbers.append(i)

    print(fav_numbers) #Modify to display the list of favourite numbers
    
    return fav_numbers#Do not remove this line


#Prompt user to enter 2 integers
start_range = int(input('Enter the starting number: '))
end_range = int(input('Enter the ending number: '))

#Do not remove the next line
favourite_number = find_favourite_numbers(start_range,end_range)

#Always have 3 elements in output
if len(favourite_number) < 3:
    favourite_number.append(0)

#input 50,150  output [70, 105, 140]
#input -35,35  output [-35, 0, 35]


