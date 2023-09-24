#Question 4 - Ct Revision

#Use a loop to determine if it is a triangular number and store in a list
triangular_numbers = []
n = 0
while n >= 0 and n <= 5000:
    trinum = ((n ** 2) + n) / 2
    triangular_numbers.append(trinum)
    n = n + 1

#Prompt user to enter a number between 0 and 5000
number = int(input("Please enter a number between 0 and 5000: "))
trinumber = ((number ** 2) + number) / 2

#Check if trinumber is in triangular_numbers list
if trinumber in triangular_numbers:
    print(number, "is a triangular number and it is the", str(len(str(trinumber))) + "th number.")
else:
    print(number, "is NOT a triangular number.")