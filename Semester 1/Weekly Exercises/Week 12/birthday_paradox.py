#An Yong Shyan, S10258126B

#Import random
import random

#Define function
def birthday():
    #Create a list to store the birthdays
    birthdays = []
    while True:
        num = random.randint(1,365)

        #Print the birthday
        print(num, 'was randomly generated.')

        #Check if there are any duplicates
        if num in birthdays:
            birthdays.append(num)
            print('Duplicate day! This took', len(birthdays), 'tries.')
            break
        else:
            birthdays.append(num)

#Call function
print('This program demonstrates the birthday paradox!')
birthday()