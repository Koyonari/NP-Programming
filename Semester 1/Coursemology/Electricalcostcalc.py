#Prompt user for electrical cost for 3 months
threemonth = str(input('Enter the electrical cost($) for 3 months separated by semicolon: '))

#Make it a list
tmnth = threemonth.split(';')

#Assign variables to all 3 elements
month1, month2, month3 = tmnth
month1 = float(month1)
month2 = float(month2)
month3 = float(month3)

#Calculate average cost and print
average_cost = (month1 + month2 + month3) / 3
print('Average electrical cost($):' , average_cost)
