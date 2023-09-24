#An Yong Shyan, S10258126B

numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]
unique = []

#For loop to get odd numbers into the list
for num in numbers:
    if len(unique) < 5 and num % 2 != 0 and num not in unique:
        unique.append(num)
    
print(unique)