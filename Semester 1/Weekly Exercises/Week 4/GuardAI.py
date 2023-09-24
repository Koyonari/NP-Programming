#An Yong Shyan 10258126B

#Prompt user if guard sees player
sees_player = str(input('Does the guard see the player (y/n)? '))

if sees_player == 'y':
    dist_from_player = int(input('How far away is the player? '))
    if dist_from_player <= 1:
        print('The guard attacks! ')
    elif 2 <= dist_from_player <= 4:
        print('The guard advances. ')
    elif dist_from_player >= 5:
        print('The guard waits. ')
elif sees_player == 'n':
    print('The guard waits. ')