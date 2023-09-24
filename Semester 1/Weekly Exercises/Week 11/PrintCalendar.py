#An Yong Shyan, S10258126B

#Thought Process
#1. Prompt user for number of days in month and which day of the week it starts on
#2. Print the days of a week
#3. Print the dates of the month using a nested for loop

#Code

# Prompt user for number of days and first day of the week
days = int(input('Enter number of days: '))
first_day = input('When is the first day of the week: ')

# Create a list of days of the week
weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# Determine the index of the first day of the week
first_day_index = weekdays.index(first_day)

# Print Days of the week
print(' '.join(weekdays))

# Print Dates of the month
day_counter = 1
for week in range((days + first_day_index) // 7 + 1):
    week_dates = []
    for day in range(7):
        if week == 0 and day < first_day_index:
            week_dates.append('   ')
        elif day_counter > days:
            break
        else:
            week_dates.append(f'{day_counter:3d}')
            day_counter += 1
    print(' '.join(week_dates))
