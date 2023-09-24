# An Yong Shyan, 10258126B

#Prompt user for marks
grade = float(input("Enter your marks: "))
if grade >= 85 and grade <= 100:
    print("Grade: A+")
    print("Excellent!")
elif grade >= 80 and grade < 85:
    print("Grade: A")
    print("Well done.")
elif grade >= 75 and grade < 80:
    print("Grade: B+")
elif grade >= 70 and grade < 75:
    print("Grade: B")
elif grade >= 65 and grade < 70:
    print("Grade: C+")
elif grade >= 60 and grade < 65:
    print("Grade: C")
elif grade >= 55 and grade < 60:
    print("Grade: D+")
elif grade >= 50 and grade < 55:
    print("Grade: D")
elif grade >= 0 and grade < 50:
    print("Grade: F")
    print("See me.")
else:
    print("Stop cheating sia.")