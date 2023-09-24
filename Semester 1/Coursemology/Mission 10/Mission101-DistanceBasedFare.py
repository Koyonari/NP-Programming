#Programming I
###########################
#      Mission 10.1       #
#   Distance Based Fare   #   
###########################
#Background
#==========
#Distance-Based Fares (DBF) is a fare payment scheme currently used across public buses and MRT/LRT trains in Singapore.
#Fares are charged based on the total distance travelled (regardless if it is on a bus or train).
#The distance-based fare calculation is available in the distance-based-fare.csv file provided.
#Based on the route details of bus service 174 (bus_174.csv), write a program to meet the following requirements:
#a) Calculate the distance travelled based on the boarding and alighting bus stop
#b) Calculate the payable fare
#Return the result of the above answers in a list of two items (e.g., [29.0,1.90])
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   board, alight, distance, fare

board = input('Enter boarding busstop: ')
alight = input('Enter alighting busstop: ')

#board CODING FROM HERE
#======================
#Create your function here
def calculate_fare(board,alight):
    file = open("distance-based-fare.csv")
    distance_data = file.read().splitlines()[1:]
    distance_data = [x.split(',') for x in distance_data]
    file.close()
    file = open("bus_174.csv")
    data = file.read().splitlines()[1:]
    data = [x.split(',') for x in data]
    bus_data = {stop_no:float(dist) for dist, stop_no, _, _ in data}
    file.close()
    distance = bus_data[alight] - bus_data[board]
    for i in range(len(distance_data)):
        if float(distance_data[i][0]) >= distance:
            fare = float(distance_data[i][1])
            break
    else:
        fare = float(distance_data[-1][1])
    # Convert to dollar
    fare = fare / 100
    return [distance, fare]
    
#Statement to call the function and print the result
#Remove the statement when submitting in Coursemology 
print(calculate_fare(board, alight))
#input 22009,10499 output [29.0, 1.9]
#input 28169,42059 output [9.2, 1.29]
#input 42089,10041 output [16.9, 1.61]