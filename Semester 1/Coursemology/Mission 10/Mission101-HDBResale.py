#Programming I
#########################
#      Mission 10.1     #
#   HDB Resale Prices   #   
#########################
#Background
#==========
#Tom is conducting some research into HDB resale prices as part of his part-time work for a real estate agency.
#Write a program to find out the following:
#
#a) The 2022 average price for the 4-room flat type (in 2 decimal places)
#b) The number of transactions above the average resale prices in part (a)
#c) The town with the highest resale price for the 5-room flat type in 2022
#
#Return the result of the three parts in a list of 3 items (e.g., [34535.35,20,'Hougang']
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   four_room_average, above_average, town_highest
#Set the filename
#Remove this statement when submitting in Coursemology
filename = ".\\Week 13\\Coursemology\\HDB-Resale-Price.csv"
#START CODING FROM HERE
#======================
#Create your function here
def ReadCSV(filename):
    file = open(filename)
    # Load data into memory
    data = file.read().splitlines()
    data = [x.split(',') for x in data]
    file.close()

    # Clense data so there is only 2022 left
    data = [x for x in data if x[0].startswith("2022")]

    #Part a
    four_rooms = [x for x in data if x[2] == "4-room"]  # Get the 4 room flats
    average_prices = [int(x[3]) for x in four_rooms if x[3].isdigit()]
    four_room_average = round(sum(average_prices) / len(average_prices), 2)

    #Part b
    above_average = [x for x in average_prices if x > four_room_average]
    above_average = len(above_average)

    #Part c
    five_rooms = [x for x in data if x[2] == "5-room"]
    five_prices = [(int(x[3]), x[1]) for x in five_rooms if x[3].isdigit()]
    town_highest = max(five_prices)[1]
    return [four_room_average, above_average, town_highest]
    
#Statements to call the function, save result in variable result and print out
#to double-check your result returned from function
#Remove these statements when submitting in Coursemology
result = ReadCSV(filename)
print(result)
#output [566969.47, 29, 'QUEENSTOWN']