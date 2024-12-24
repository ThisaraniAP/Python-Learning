EngTest=int(input("Please input the english test score: "))
MathTest=int(input("Please input the maths test score: "))

if EngTest<40 and MathTest<50:
    print("Student failed both tests.")
elif EngTest<40 or MathTest<50:
    print("Student failed one test. ")
elif EngTest>=80 and MathTest>=85:
    print("Student has passed both tests with distinction.")
else:
    print("Student passed both tests.")
    
