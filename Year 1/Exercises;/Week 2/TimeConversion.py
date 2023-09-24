secs = int(input("Please enter the time to be converted, in sec: "))
hrs = secs // 3600
mins = (secs % 3600) // 60
finalsecs = (secs % 3600) % 60
print('Time: ' + str(hrs) + 'hr, ' + str(mins) + ' min ' + str(finalsecs) + ' sec')