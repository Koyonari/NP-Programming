#An Yong Shyan, S10258126B

#Prompt user for number of days

days = int(input("Enter number of days: "))

# Utilize a for loop to print the days and tasks
loops = 1

for count in range(days):

    if count % 7 == 0:
        print('Day | Task(s)')

    print(f'{count + loops:3} |')