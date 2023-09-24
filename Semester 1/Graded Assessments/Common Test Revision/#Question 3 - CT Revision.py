#Question 3 - CT Revision

#Thinking Process
#1. Create name list
#2. Create weight list
#3. Create height list
#4. Create size list
#5. Calculate bmi
#6. Create bmi list
#7. Format

#Create 4 lists
name_list = ['Sharon', 'Mic', 'Josh','Hannah','Hanzel']
height_list = ['172', '166', '187', '200', '166']
weight_list = ['59.5', '65.6', '49.8', '64.2', '47.5']    
size_list = ['M', 'L', 'S', 'M', 'S']

#Calculate BMI
bmi_list = []
for i in range(0, len(name_list)):
    bmi = float(weight_list[i]) / ((float(height_list[i]) / 100) ** 2)
    bmi = round(bmi, 2)
    bmi_list.append(bmi)

#Print and format
print('{:10} {:10} {:11} {:8} {:4}'.format('Name', 'Weight', 'Height', 'BMI', 'Size'))
print('{:10} {:10} {:11} {:5} {:>4}'.format(name_list[0], weight_list[0], height_list[0], bmi_list[0], size_list[0]))
print('{:10} {:10} {:11} {:5} {:>4}'.format(name_list[1], weight_list[1], height_list[1], bmi_list[1], size_list[1]))
print('{:10} {:10} {:11} {:5} {:>4}'.format(name_list[2], weight_list[2], height_list[2], bmi_list[2], size_list[2]))
print('{:10} {:10} {:11} {:5} {:>4}'.format(name_list[3], weight_list[3], height_list[3], bmi_list[3], size_list[3]))
print('{:10} {:10} {:11} {:5} {:>4}'.format(name_list[4], weight_list[4], height_list[4], bmi_list[4], size_list[4]))

#Prediction for t-shirt size based on BMI
