#Question 1 - CT Revision

times = input('Enter time taken of 2 laps separated by semi-colon (seconds): ')

times_list = times.split(';')

firstlap_time = times_list[0] 
secondlap_time = times_list[1] 

if firstlap_time > secondlap_time: 
    best = float(secondlap_time)
else:
    best = float(firstlap_time)

average = (float(firstlap_time) + float(secondlap_time)) / 2

print("Tom's best time is {:.1f} s and average time is {} s".format(best, average))
