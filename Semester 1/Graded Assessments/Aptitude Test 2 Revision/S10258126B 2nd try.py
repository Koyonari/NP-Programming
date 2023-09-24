#Aptitude test 2 Revision

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
