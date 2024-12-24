Square=0
Cube=0
Number=int(input("Please enter the number: "))

while Number>=1 and Number<=50:
    Square=Number*Number
    Cube=Number*Number*Number
    
    print("The number you entered is: ", Number)
    print("The square of the number is: ", Square)
    print("The cube of the number is: ", Cube)

    Number=int(input("Please enter the number: "))
    
