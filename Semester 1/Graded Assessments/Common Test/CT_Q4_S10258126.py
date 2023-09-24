#An Yong Shyan (S10258126) - IT03

#Create list
list = [['Curry puff', '2.40', '2'],
        ['Apple tart', '2.00', '4'],
        ['Tuna puff', '2.20', '5'],
        ['Egg tart', '1.80' , '1'],
        ['Custard tart', '1.50', '2']]

#Curry puff
curry = list[0]
price = curry[1]
quantity = curry[2]
curry_amount = float(price) * float(quantity)
curry.append(str(curry_amount))

#Apple tart
apple = list[1]
price = apple[1]
quantity = apple[2]
apple_amount = float(price) * float(quantity)
apple.append(str(apple_amount))

#Tuna puff
tuna = list[2]
price = tuna[1]
quantity = tuna[2]
tuna_amount = float(price) * float(quantity)
tuna.append(str(tuna_amount))

#Egg tart
egg = list[3]
price = egg[1]
quantity = egg[2]
egg_amount = float(price) * float(quantity)
egg.append(str(egg_amount))

#Custard tart
custard = list[4]
price = custard[1]
quantity = custard[2]
custard_amount = float(price) * float(quantity)
custard.append(str(custard_amount))

#Total cost
tart = apple_amount + egg_amount + custard_amount
puff = curry_amount + tuna_amount

#Print
print('{:13} {:13} {:11} {:8}'.format('Item Name', 'Unit Price', 'Quantity', 'Amount'))
print('{:19} {:14} {:7} {:1}'.format(curry[0], curry[1], curry[2], curry[3]))
print('{:19} {:14} {:7} {:1}'.format(apple[0], apple[1], apple[2], apple[3]))
print('{:19} {:14} {:6} {:1}'.format(tuna[0], tuna[1], tuna[2], tuna[3]))
print('{:19} {:14} {:7} {:1}'.format(egg[0], egg[1], egg[2], egg[3]))
print('{:19} {:14} {:7} {:1}'.format(custard[0], custard[1], custard[2], custard[3]))

print('\nTotal cost of tarts: ${:.2f}'.format(tart))
print('Total cost of puffs: ${:.2f}'.format(puff))
