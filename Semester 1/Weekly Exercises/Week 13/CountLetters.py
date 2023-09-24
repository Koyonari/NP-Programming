#An Yong Shyan, S10258126B

#Prompt user to input a sentence
sen = input("Enter a sentence: ")

#Make a new dictionary
sen_dict = {}

#Remove punctuations and spaces and add to dictionary
for char in sen:
    char = char.lower()
    if char.isalpha():
        if char not in sen_dict:
            sen_dict[char] = 0
        sen_dict[char] += 1

#Print the dictionary
for key, value in sen_dict.items():
    print(key, ':', value)