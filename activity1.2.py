def factorial(num):
    ans = 1
    num += 1
    for n in range(1, num):
        ans = ans * n
    return ans

try:
    number = int(input("Enter a number: "))
except:
    print("Invalid input.")
else:
    if number > 0:
        fac = factorial(number)
        print("The factorial of your number is: ", fac)
    else:
        print("Invalid input.")
