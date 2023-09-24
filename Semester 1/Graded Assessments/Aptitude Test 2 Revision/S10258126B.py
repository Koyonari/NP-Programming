#An Yong Shyan (S10258126B) - IT03
#Question 1 Part a)
#Read file
f = open('sales.txt', 'r')
lines = f.readlines()

data = []

#Remove whitespace and split
for line in lines:
    line = line.strip().split(',')
    data.append(line)

#Print list
print(data, '\n')

#Close file
f.close()

#Question 1 Part b)

#Thought Process
#1. Create product list and empty list for total units sold
#2. Use a for loop and format to print sales.txt
#3. Add up units sold for each product and append to total_units_list
#4. Print out headers and use a for loop to print out product list and total units sold lists while formatting

#Create lists
product_list = ['MacBook Air', 'MacBook Pro', 'iMac']
total_units_list = {'MacBook Air': None, 'MacBook Pro': None, 'iMac': None}

#Print sales.txt and first section
for i in data[:]:
    print('{:15} {:15} {:10}'.format(*i))

#Second section
#Print headers
print('\n' + '{:15} {:15}'.format('Product', 'Total Units Sold'))

#Get the units sold from lines
total_units_list = [0, 0, 0]

for i, product in enumerate(product_list):
    for sold in data[1:]:
        if sold[1] == product:
            total_units_list[i] += int(sold[2])

#For loop to print out total
y = 0
for x in product_list:
    print('{:15} {:1}'.format(product_list[0], total_units_list[y]))
    y += 1
