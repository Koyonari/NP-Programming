# An Yong Shyan, 10258126B

#Prompt user to input original string and substring to delete
og = str(input('Enter original string: '))
sub = str(input('Substring to delete: '))

#Remove substring from original string
modified = og.replace(sub, '', 1)
print('The modified string is:' , modified)