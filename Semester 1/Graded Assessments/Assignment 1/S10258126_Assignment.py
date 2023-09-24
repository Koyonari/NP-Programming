#An Yong Shyan, S10258126B, IT03, 13 August 2023


#Import library
import csv
from operator import itemgetter

#Define functions for all Basic Requirements

#Read data from carpark-information and store in a list and dictionary
def read_carpark_info():
    carpark_list = []

    #Read file
    with open('carpark-information.csv', 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')

        #For loop to append value of key-pair value to carpark_list
        for line in lines[1:]:
            values = line.strip().replace('"', '').split(',', 3)
            carpark_info = {}
            for i in range(len(headers)):
                carpark_info[headers[i]] = values[i]
            carpark_list.append(carpark_info)
    return carpark_list

#Option 1
def display_total_carparks(carpark_list):
    print('Option 1: Display Total Number of Carparks in "carpark-information.csv"')
    print('Total Number of carparks in "carpark-information.csv":', str(len(carpark_list)) + '.\n')

#Option 2
def display_basement_carparks(carpark_list):
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    print('Carpark No Carpark Type       Address')
    
    #Make new variable as q for the number of Basement Car Parks
    q = 0

    #Use a for loop and if else statement to check if its a Basement Car Park to print
    for carpark in carpark_list:
        if carpark['Carpark Type'] == 'COVERED CAR PARK':
            q += 1
            print('{:10} {:18} {:27}'.format(carpark['Carpark Number'], carpark['Carpark Type'], carpark['Address']))
    print('Total number:', q, '\n')

#Option 3
def read_availability_file():
    print('Option 3: Read Carpark Availability Data File')
    file_name = input('Enter the file name: ')
    if file_name == 'carpark-availability-v1.csv' or file_name == 'carpark-availability-v2.csv':
        with open(file_name, 'r') as data:
            data = data.readline() #Read first line only
        print(data)
    else:
        print('Invalid file\n')
    return file_name

#Option 4
def print_total_carparks(file_name):
    print('Option 4: Print Total Number of Carparks in the File Read in [3]')
    #Read file from Option 3 and use len to get the number of carparks, Minus 2 as the first 2 lines are headers
    with open(file_name, 'r') as data:
        data = data.readlines() #Read all lines and store in a list
    print('Total Number of Carparks in the File:', len(data) - 2, '\n')

#Option 5
def display_carparks_without_lots(file_name):
    print('Option 5: Display Carparks Without Available Lots')
    #u is to count the number of full lots by increasing by 1 every time the for loop is looped
    u = 0
    with open(file_name, 'r') as lots:
        lots_lines = lots.readlines()
        lots_lines = lots_lines[2:]
        #Use a for loop to read file from option 3
        for lines in lots_lines:
            splitted = lines.split(',')
            available_lots = int(splitted[2])
            #Use a if statement to make print carpark number with 0 available lots
            if available_lots == 0:
                print('Carpark Number:', splitted[0])
                u += 1
        print('Total number:', u, '\n')

#Option 6
def display_carparks_x_percent(file_name):
    print('Option 6: Display Carparks With At Least x% Available Lots')
    percentage = float(input('Enter the percentage required: '))
    #v is the total number of carparks with x% available lots
    v = 0
    #Make a empty list for the nested list later
    l_list = []
    #Read file and find percentage of available lots to total lots
    with open(file_name, 'r') as l:
        l = l.readlines()
        l = l[2:]
        for b in l:
            c = b.strip().split(',')
            l_list.append(c)
        #For loop and if statement to print out carpark details if >= percentage
        print('Carpark No  Total Lots  Lots Available  Percentage')
        for p in l_list:
            available = int(p[2])
            total = int(p[1])
            #For more than 0 total lots
            if total > 0:
                lots_percent = (available / total) * 100
                if lots_percent >= percentage:
                    print('{0:10} {1:>11} {2:>15} {3:>11.1f}'.format(p[0], p[1], p[2], lots_percent))
                    v += 1
            #For 0 total lots
            else:
                continue
        #Print total number of carparks with x% available lots
        print('Total number:', v, '\n')

#Option 7
def display_carpark_addresses_x_percent(file_name, carpark_list):
    print('Option 7: Display Addresses of Carparks With At Least x% Available Lots')
    percentage = float(input('Enter the percentage required: '))
    #v is the total number of carparks with x% available lots
    v = 0
    #Make a empty list for the nested list later
    l_list = []
    #Read file and find percentage of available lots to total lots
    with open(file_name, 'r') as l:
        l = l.readlines()
        l = l[2:]
        for b in l:
            c = b.strip().split(',')
            l_list.append(c)
        #For loop and if statement to print out carpark details if >= percentage
        print('Carpark No  Total Lots  Lots Available  Percentage  Address')
        for p in l_list:
            available = int(p[2])
            total = int(p[1])
            #For more than 0 total lots
            if total > 0:
                lots_percent = (available / total) * 100
                if lots_percent >= percentage:
                    for carpark in carpark_list:
                        if carpark['Carpark Number'] == p[0]:
                            print('{0:10} {1:>11} {2:>15} {3:>11.1f}  {4:>8}'.format(p[0], p[1], p[2], lots_percent, carpark['Address']))
                            v += 1
            #For 0 total lots
            else:
                continue
        #Print total number of carparks with x% available lots
        print('Total number:', v, '\n')

#End of Basic Requirements

#-------------------------------------------------------------------------------------------------------------------------------------------------

#Advanced Requirements

#Option 8
def display_all_carparks(file_name, carpark_list):
    print('Option 8: Display All Carparks at Given Location')
    location = input('Enter a location: ')
    location = location.upper()
    #v is the total number of carparks
    v = 0
    #Make a empty list
    availability_nested_list = []
    
    #Read file and append to the empty list
    with open(file_name, 'r') as datafile:
        data = datafile.readlines()
        data = data[2:]
        for availability in data:
            availability_list = availability.strip().split(',')
            availability_nested_list.append(availability_list)

    #For loop and if statement to print out carpark details
    print('Carpark No  Total Lots  Lots Available  Percentage  Address')
    for z in availability_nested_list:
        #Turn from string to integer for calculation later
        available = int(z[2])
        total = int(z[1])
        #For more than 0 total lots
        if total > 0:
            lots_percent = (available / total) * 100
            for carpark in carpark_list:
                if location in carpark['Address'] and carpark['Carpark Number'] == z[0]:
                    print('{0:10} {1:>11} {2:>15} {3:>11.1f}  {4:<8}'.format(z[0], z[1], z[2], lots_percent, carpark['Address']))
                    v += 1
            #For 0 total lots
        else:
            continue
        #Print total number of carparks with x% available lots
    if v != 0:
        print('Total number:', v, '\n')
    else:
        print('{0:10} {1:>11} {2:>15} {3:>11}  {4:9}'.format('NIL', 'NIL', 'NIL', 'NIL', 'NIL'))
        print('No carpark found.\n')

#Option 9
#Display 1 carpark with the highest available lots, 1 carpark with the highest total lots or 1 carpark with the highest percentage of available lots
def display_parking_lots(file_name, carpark_list):
    #Make empty lists to use zip later
    file_list = [] #Nested list of file_name details
    carparkno_list = [] #List of carpark numbers
    carparktype_list = [] #List of carpark type
    carparkparkingsystem_list = [] #List of parking system
    carparkaddress_list = [] #List of addresses
    carparktotal_list = [] #List of total lots
    carparkavailable_list = [] #List of available lots
    carparkpercentage_list = [] #List of percentage available for lots

    with open(file_name, 'r') as parking:
        parking = parking.readlines()
        parking = parking[2:] #Get rid of headers
        for lots in parking:
            lots = lots.strip().split(',')
            file_list.append(lots) #Nested list of file_name details
    for data in file_list:
        carparktotal_list.append(int(data[1]))
        carparkavailable_list.append(int(data[2]))
        #If statement for when total number of lots is 0
        if int(data[2]) > 0:
            percentage_of_available = int(data[2]) / int(data[1]) * 100
        else:
            continue
        carparkpercentage_list.append(percentage_of_available)

    for carpark_details in carpark_list:
        carparkno_list.append(carpark_details['Carpark Number'])
        carparktype_list.append(carpark_details['Carpark Type'])
        carparkparkingsystem_list.append(carpark_details['Type of Parking System'])
        carparkaddress_list.append(carpark_details['Address'])
    final_list = list(zip(carparkno_list, carparktype_list, carparkparkingsystem_list, carparkaddress_list, carparktotal_list, carparkavailable_list, carparkpercentage_list))

    totalavailablepercentage = input('Total Carpark Lots / Available Carpark Lots / Percentage of Available Carpark Lots? ')
    #Give user option to sort by total, available or percentage
    if 'total' in totalavailablepercentage.lower():
        final_list = sorted(final_list, key = itemgetter(4), reverse = True)
    elif 'available' in totalavailablepercentage.lower():
        final_list = sorted(final_list, key = itemgetter(5), reverse = True)
    elif 'percent' in totalavailablepercentage.lower():
        final_list = sorted(final_list, key = itemgetter(6), reverse = True)
    else:
        print('Please enter valid option.')

    if 'total' in totalavailablepercentage.lower():
        elements = final_list[0]
        print('Carpark with Highest Number of Parking Lots')
        print('-------------------------------------------')
        print('Carpark Number:', elements[0])
        print('Carpark Type:', elements[1])
        print('Type of Parking System', elements[2])
        print('Address:', elements[3])
        print('Total lots:', elements[4])
        print('Available lots:', elements[5])
        print('Percentage of available lots: {:.1f}\n'.format(elements[6]))
    
    elif 'available' in totalavailablepercentage.lower():
        elements = final_list[0]
        print('Carpark with Highest Number of Available Parking Lots')
        print('-------------------------------------------')
        print('Carpark Number:', elements[0])
        print('Carpark Type:', elements[1])
        print('Type of Parking System', elements[2])
        print('Address:', elements[3])
        print('Total lots:', elements[4])
        print('Available lots:', elements[5])
        print('Percentage of available lots: {:.1f}\n'.format(elements[6]))

    elif 'percent' in totalavailablepercentage.lower():
        elements = final_list[0]
        print('Carpark with Highest Percentage of Available Parking Lots')
        print('-------------------------------------------')
        print('Carpark Number:', elements[0])
        print('Carpark Type:', elements[1])
        print('Type of Parking System', elements[2])
        print('Address:', elements[3])
        print('Total lots:', elements[4])
        print('Available lots:', elements[5])
        print('Percentage of available lots: {:.1f}\n'.format(elements[6]))
    
            
#Option 10
#Create an Output File that includes file_name with addresses and sorts by lots available ascendingly
def output_file(file_name, carpark_list):
    print('Option 10: Create Output File with Carpark Availability with Addresses and Sort by Lots Available')
    output_file_name = input('Enter output file name (include .csv at the end): ')

    #Create empty lists to store carpark details and count
    carpark_nos = []
    carpark_total_lots = []
    carpark_available_lots = []
    carpark_address = []
    count = 2
    
    #Read in the carpark availability data
    with open(file_name, 'r') as availability_file:
        availability_lines = availability_file.readlines()
        timestamp = availability_lines[0]
        availability_lines = availability_lines[2:]
        for line in availability_lines:
            carpark_num, total_lots, available_lots = line.strip().split(',')
            for carpark in carpark_list:
                if carpark['Carpark Number'] == carpark_num:  #If statement to check if the value in the key-value pair for Carpark Number is the same as carpark_num
                    carpark_nos.append(carpark_num)
                    carpark_total_lots.append(int(total_lots))
                    carpark_available_lots.append(int(available_lots))
                    carpark_address.append(carpark['Address'])
                else:
                    continue
    
    #Combine all details
    output_data = list(zip(carpark_nos, carpark_total_lots, carpark_available_lots, carpark_address))

    #Sort the data by available lots in ascending order
    output_data.sort(key = lambda x: x[2])

    #Write the data to the output file
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow([timestamp])
        writer.writerow(['Carpark Number', 'Total Lots', 'Lots Available', 'Address'])
        for row in output_data:
            writer.writerow(row)
            count += 1

    print(output_file_name, 'created successfully with', count, 'lines.\n')



#End of Advanced Requirements
#-------------------------------------------------------------------------------------------------------------------------------


#Main Code
carpark_list = read_carpark_info()

#Display main menu
option = 11
while option != 0:
    print('\nMENU')
    print('====')
    print("[1]  Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2]  Display All Basement Carparks in 'carpark-information.csv'")
    print('[3]  Read Carpark Availability Data File')
    print('[4]  Print Total Number of Carparks in the File Read in [3]')
    print('[5]  Display Carparks Without Available Lots')
    print('[6]  Display Carparks With At Least x% Available Lots')
    print('[7]  Display Addresses of Carparks With At Least x% Available Lots')
    print('[8]  Display All Carparks at Given Location')
    print('[9]  Display Carpark with the Most Parking Lots')
    print('[10] Create Output File with Carpark Availability with Addresses and Sort by Lots Available')
    print('[0]  Exit')

    #Prompt user for option number
    option = int(input('Enter your option: '))
    #Assign choice to a number
    choice  = 11
    if option == 1:
        display_total_carparks(carpark_list)
    elif option == 2:
        display_basement_carparks(carpark_list)
    elif option == 3:
        file_name = read_availability_file()
        while choice != 0:
            #Open menu to get option again and assign to different variable to not confuse with option
            print('MENU')
            print('====')
            print("[1]  Display Total Number of Carparks in 'carpark-information.csv'")
            print("[2]  Display All Basement Carparks in 'carpark-information.csv'")
            print('[3]  Read Carpark Availability Data File')
            print('[4]  Print Total Number of Carparks in the File Read in [3]')
            print('[5]  Display Carparks Without Available Lots')
            print('[6]  Display Carparks With At Least x% Available Lots')
            print('[7]  Display Addresses of Carparks With At Least x% Available Lots')
            print('[8]  Display All Carparks at Given Location')
            print('[9]  Display Carpark with the Most Parking Lots')
            print('[10] Create Output File with Carpark Availability with Addresses and Sort by Lots Available')
            print('[0]  Exit')

            #Prompt user for choice instead of option
            choice = int(input('Enter your option: '))
            if choice in [4, 5, 6, 7, 8, 9, 10]:
                if choice == 4:
                    print_total_carparks(file_name)
                elif choice == 5:
                    display_carparks_without_lots(file_name)
                elif choice == 6:
                    display_carparks_x_percent(file_name)
                elif choice == 7:
                    display_carpark_addresses_x_percent(file_name, carpark_list)
                elif choice == 8:
                    display_all_carparks(file_name, carpark_list)
                elif choice == 9:
                    display_parking_lots(file_name, carpark_list)
                elif choice == 10:
                    output_file(file_name, carpark_list)
                elif choice == 0:
                    print('Exit')
                    break
    elif option == 0:
        print('Exit')
    elif option == 4 or option == 5 or option == 6 or option == 7 or option == 8 or option == 9 or option == 10:
        print('Please select Option 3 first.\n')
    else:
        print('Please select valid option.\n')
