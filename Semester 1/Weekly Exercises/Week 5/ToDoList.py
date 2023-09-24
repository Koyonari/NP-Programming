#Open text file in read mode
file = open('todo.txt', 'r')

#For loop to read 3 lines
for i in range(3):
    line = file.readline()
    print(line, end = '')
