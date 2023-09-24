#An Yong Shyan, S10258126B

#Prompt user to enter a number
num = int(input("Please enter a number: "))

#Use a while loop to times 1 to 10
multiplier = 1

while multiplier <= 10:
    print('   ' + str(num), "x", multiplier, "=", num * multiplier)
    multiplier += 1

#Print the end
print('The End')