emp_no = int(input("Enter the employee number: "))
hrs = int(input("Enter the hours worked: "))
rate = int(input("Enter the hourly rate: "))

if hrs > 40:
    gw = (40 * rate) + ((hrs - 40) * rate * 1.5)
else:
    gw = hrs * rate

print ("Employee number: ", emp_no)
print ("Gross wage: ", gw)
