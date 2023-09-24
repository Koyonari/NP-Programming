#An Yong Shyan, 10258126B

#Create list of friends
friends = ['Izzat', 'Bryan', 'Dalton', 'Ethan', 'Isaac']

#Prompt user for new name and append
new = input('What is the name of your new friend? ')
friends.append(new)
print('My friends are: ', friends)

#Prompt user to input existing name
friendzone = input('Who do you want to friendzone? ')
friendzone_position = friends.index(friendzone)
print('{} was in position {}. He will be friendzoned.'.format(friends[friendzone_position], friendzone_position))

#Remove friendzoned from friends list
friends.pop(friendzone_position)
print('My eligible friends are now:', friends)
