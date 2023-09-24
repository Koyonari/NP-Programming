#Question 2 - CT Revision

#Prompt user to enter 3 cards
card1 = int(input('Enter card 1: '))
card2 = int(input('Enter card 2: '))
card3 = int(input('Enter card 3: '))

total = card1 + card2 + card3

#Determine if ace is 1 or 11
if card1 == 1 and total >= 21:
        card1 = 11
elif card2 == 1 and total >= 21:
        card2 = 11
elif card3 == 1 and total >= 21:
        card3 = 11

if card1 == 11 or card1 == 12:
    card1 = 10
elif card2 == 11 or card2 == 12:
    card2 = 10
elif card3 == 11 or card3 == 12:
    card3 = 10

total = card1 + card2 + card3

#Print out total value
print('Total value is', total)