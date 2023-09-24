#An Yong Shyan, S10258126B

#Prompt user for pin
pin = input('Enter PIN: ')

#While loop to check if pin is valid
tries = 2
if pin != '123':
    while tries > 0:
        print('Invalid PIN. Please try again.')
        print('You have {} tries left.'.format(tries))
        pin = input('Enter PIN: ')
        tries -= 1
        if tries <= 0:
            print('Invalid PIN. You have no more tries.')
            print('Your account is locked.')
            break
else:
    print('PIN accepted.')