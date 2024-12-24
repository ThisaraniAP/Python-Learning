define variable num, ans
define function factorial(num)
	ans = 1
	num = num + 1
	for n in range(1, num)
		ans = ans * n
	return ans
try
	number = convert_to_integer(input (“Enter your number: ”))
except
	display(“Invalid output.”)
else
	if number > 0
		fac – factorial(number)
		display(“The factorial of your number is: ” + fac)
	else
		display(“Invalid output.”)