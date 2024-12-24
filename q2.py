base=50
heightChk="TRUE"

while heightChk=="TRUE":
    height=int(input("Enter the height(between 1 and 100): "))
    if height>=1 and height<=100:
        heightChk="FALSE"

area=0.5*base*height

print("Base of triangle is: ", base)
print("Height of triangle is: ", height)
print("Area of triangle is: ", area)
