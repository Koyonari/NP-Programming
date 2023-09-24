#An Yong Shyan, S10258126B

#Thought Process
#1. Create a nested list
#2(i)   Use a for loop to print the nested list using index
#2(ii)  In the for loop, print the grid before the next row
#2(iii) Print the last grid after the for loop

#Code

#Map stored in a nested list
map = [ ['T', ' ', ' ', ' ', 'T'],\
        [' ', 'P', ' ', ' ', ' '],\
        [' ', ' ', ' ', 'T', ' '],\
        [' ', 'T', ' ', ' ', ' ']]

#For loop to print grid and element
for row in range(len(map)):
    print('+---' * len(map[row])+'+')
    for element in map[row]:
        print('|', element, end=' ')
    print('|')
print('+---' * len(map[0])+ '+')