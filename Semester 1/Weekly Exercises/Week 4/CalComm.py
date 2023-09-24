# An Yong Shyan, 10258126B
#Prompt user for montly sales
monthly_sales = int(input('Enter montly sales of sales agent: '))

#Calculate the commision rate
if monthly_sales >= 10000:
    commision_rate = 10
else:
    commision_rate = 5

#Display commision rate and commision paid
print('The commision rate is:', commision_rate, '%')
print('The commision paid is: $', monthly_sales * commision_rate / 100)