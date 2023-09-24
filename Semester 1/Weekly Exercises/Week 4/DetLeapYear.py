#An Yong Shyan, 10258126B

#Prompt user to input year
year = int(input('Please enter the year: '))

#Check if it is a leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
    print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.')