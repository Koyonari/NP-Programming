#An Yong Shyan, S10258126B

#Prompt user for word
words = []
total_letters = 0
count = 0

while count < 5:
    word = input('Enter a word (x to exit): ')
    
    if word == 'x':
        break
    
    if word in words:
        print(word, 'has already been entered.')
        continue
    
    words.append(word)
    total_letters += len(word)
    count += 1

print('Your words are', words)


print('The number of letters in these words is', total_letters)
