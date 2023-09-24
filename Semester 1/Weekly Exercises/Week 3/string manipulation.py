#Prompt user for original and delete
original_str = input('Enter original string: ')
delete_str = input('Substring to delete: ')

#Find index to delete
index = original_str.find(delete_str)
print(index)

#Left substring
left_str = original_str[0:index]
print(left_str)

#Right substring
right_str = original_str[index + len(delete_str):]
print(right_str)

new_str = left_str + right_str

print('The modified string is : (0)'.formate(new_str))
