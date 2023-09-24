file = open('data.txt', 'r')

sum = 0
num_students = 0
for line in file:
    value = int(line.split(',')[1])
    assert value >= 0
    sum += value
    num_students += 1

print('Average:', sum / num_students)
file.close()