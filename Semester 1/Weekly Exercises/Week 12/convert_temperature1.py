#An Yong Shyan, S10258126B

#Define function
def convert_temperature():
    f = (c * 9 / 5) + 32
    return f

#Prompt user for temperature
c = float(input("Enter the temperature in degree celsius: "))

#Print result
print('The temperature is equivalent to', convert_temperature(), 'degree fahrenheit.')