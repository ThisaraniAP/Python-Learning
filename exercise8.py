s_amount = int(input("Enter the sales amount: "))

if s_amount >= 1000:
    discount = s_amount*10/100
else:
    discount = s_amount*5/100
    
net = s_amount - discount
print("Discount: ", discount)
print("Net amount: ", net)
