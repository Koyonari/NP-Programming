#An Yong Shyan, 10258126B

#Read file
file = open('StudentData.txt', 'r')
print('\nName \t\t  Mobile Contact')

#Print name and contacts of first student
student = file.readline()
student = student.strip('\n')
split = student.split(',')
print(split[0], '\t', split[1])

#Print name and contacts of second student
student = file.readline()
student = student.strip('\n')
split = student.split(',')
print(split[0], '\t', split[1])
