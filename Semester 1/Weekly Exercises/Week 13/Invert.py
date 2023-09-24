#An Yong Shyan, S10258126B

#Read the file
directory = 'C:\\Ngee Ann\\Semester 1\\Programming\\Week 13\\'
color = open(directory + 'colors.csv', 'r')

#Create a dictionary
colors_dict = {}
for line in color:
    name, color = line.strip().split(',')
    colors_dict[name] = color

#Use a for loop to append to new dictionary
new_colors = {}
for key, value in colors_dict.items():
    if value not in new_colors:
        new_colors[value] = []
    new_colors[value].append(key)

#Print the new dictionary
print(new_colors)