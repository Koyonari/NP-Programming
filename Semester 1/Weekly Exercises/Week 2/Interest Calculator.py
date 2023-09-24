#InterestCalculator.py
#this program calculates the interest based on given principal,
#rate and duration. 

#assigning values to the variables
principal = 10000.00	# in dollars
rate = 10
durations = 2		# in years
		
#compute the interest
interest = principal * rate / 100 * durations
		
#display the output
print('Principal ($)  : {:.2f}'.format(principal))
print('Rate(percent)  : {:.2f}'.format(rate))
print('Duration (yrs) : {:d}'.format(durations))
print('Interest  ($) : {:.2f}'.format(interest))
