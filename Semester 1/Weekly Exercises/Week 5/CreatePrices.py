#An Yong Shyan, S10258126B

#List of shop prices
prices = [["kopi", 0.4], ["teh", 0.4], ["milo", 0.5], ["soft drinks", 1.20]]
str_prices = []

#Make the list become a string
for number in prices:
    str_prices.append(str(number))
    

prices = ''.join(str_prices)

#Make the prices same format as the sample output
prices = prices.replace('][', '0\n')
prices = prices.replace('[', '')
prices = prices.replace(']', '')
prices = prices.replace(', ', ': $')
prices = prices.replace("'", '')
prices = prices + '0'


#Open and write a text file
path = 'C:\\Ngee Ann\\Semester 1\\Programming\\Week 5\\'
datafile = open(path + 'prices.txt', 'w')
datafile.write(prices)

datafile.close()
