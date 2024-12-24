def fibonacci(num):
        if num < 0:
                print("Invalid input.")

        n1 = 0
        n2 = 1
        
        for count in range(0, num):
                if count == 0:
                        print(n1)
                elif count == 1:
                        print(n2)
                else:
                        n3 = n1 + n2
                        print(n3)
                        n1 = n2
                        n2 = n3


try:
        n = int(input("Enter your number: "))
except:
        print("Invalid input.")
else:
        fibonacci(n)
