sn = int(input("Enter the student number: "))
avg = int(input("Enter the average: "))

if avg >= 50:
    grade = "Pass"
else:
    grade = "Fail"

print("Student number: ", sn)
print("Average: ", avg)
print("Grade: ", grade)
