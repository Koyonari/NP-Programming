#An Yong Shyan (S10258126) - IT03

#Prompt user for word in lowercase
#len(word)
#Prompt user for positions
#Split
#Use index
#Swap

#Code

#Prompt user for word
word = input('Enter your word: ')

#Get no. of char
print('Your input has', len(word),'characters')

#Prompt user for positions to swap
position = input("Input the positions of the characters to select, separated by ',': ")

#Split to get the index
first, second = position.split(',')
first = int(first)
first -= 1
second = int(second)
second -= 1
word1 = word[first]
word2 = word[second]
caps = word.upper()
caps1 = word1.upper()
scrambled = caps.replace(caps1, word2)
lower2 = word2.upper()
scrambled = scrambled.replace(lower2, word1)

#Change everything back to lowercase
scrambled = scrambled.lower()


#Print out characters using index
print("Swapping the characters '" + word1 + "' and '" + word2 + "'")
print('Scrambled word:' , scrambled)
