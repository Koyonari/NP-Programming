#An Yong Shyan, S10258126B

#Read lines from temperature.txt
path = 'C:\\Ngee Ann\\Semester 1\\Programming\\Week 6\\An Yong Shyan, S10258126B\\'
list = open(path + 'temperature.txt', 'r')
temperature = []
line = list.read().strip()
index = 0

#Split temperatures into a list, split and convert into float
temperatures = line.split(',')

while index < len(temperatures):
    temperature = temperatures[index]
    float_temperature = float(temperature)
    temperatures[index] = float_temperature
    index += 1

#Print out the temperatures
print('The temperatures are: ')
for temperature in temperatures:
    if temperature > 29:
        print(' ', temperature, '** higher than 29!!!')
    elif temperature <= 29:
        print(' ', temperature)

#Number of readings
print('\nNumber of readings:', len(temperatures))

#Calculate the average temperature
average = sum(temperatures) / len(temperatures)
print('Average temperature: {:.2f}'.format(average))