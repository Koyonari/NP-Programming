#An Yong Shyan, S10258126B

#Define function
def fahr_to_cel():
    fahr = float(input("Please enter the temperature in Fahrenheit: "))
    cel = (fahr - 32) * 5 / 9
    print("The temperature in celsius is", '{:.1f}'.format(cel), 'degrees')
    return cel

def cel_to_fahr():
    cel = float(input("Please enter the temperature in Celsius: "))
    fahr = cel * 9 / 5 + 32
    print("The temperature in fahrenheit is", '{:.1f}'.format(fahr), 'degrees')
    return fahr

#Print header
print('Temperature Conversion')
print('[1] Fahrenheit to Celsius')
print('[2] Celsius to Fahrenheit')
print('[3] Exit')
option = int(input('Please enter your option: '))

#If else statement to determine which function to call
if option == 1:
    fahr_to_cel()
elif option == 2:
    cel_to_fahr()
else:
    print('Goodbye!')