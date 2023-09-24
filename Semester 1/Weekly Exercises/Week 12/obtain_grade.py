# An Yong Shyan, S10258126B

# Mark list
mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]

# Define function
def obtain_grade(mark):
    if mark >= 84.5:
        grade = 'A+'
    elif mark >= 79.5:
        grade = 'A'
    elif mark >= 74.5:
        grade = 'B+'
    elif mark >= 69.5:
        grade = 'B'
    elif mark >= 64.5:
        grade = 'C+'
    elif mark >= 59.5:
        grade = 'C'
    elif mark >= 54.5:
        grade = 'D+'
    elif mark >= 49.5:
        grade = 'D'
    else:
        grade = 'F'

    return grade

# Print header
print("{:15} {:10} {:10}".format("Student Name", "Mark", "Grade"))

# Use a for loop to print the student name, mark, and grade
for student in mark_list:
    name = student[0]
    mark = student[1]
    grade = obtain_grade(mark)
    print("{:15} {:<10} {:<5}".format(name, mark, grade))
