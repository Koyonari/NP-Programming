#Prompt user for Loan, Annual income, Current loan, Total savings, Years to pay back loan
l = float(input('What is your desired loan amount? '))
a = float(input('What is your annual income? '))
c = float(input('What is the total value of your current loans? '))
s = float(input('What is the ttal of your savings? '))
y = float(input('How many years do you want to pay back this loan? '))

#Calculate interest rate
interest = (l + c) / (s + a * y) * 100
formatted_interest = '{:.1f}'.format(interest)

#Print interest rate
print('Your interest rate is ' + str(formatted_interest) + '%')
