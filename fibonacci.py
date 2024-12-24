define variable num, count, n1, n2, n3
define function fibonacci(num)
	if num < 0 then
		display (“Invalid input”)
	n1 = 0
	n2 = 1
	for count in range(0, num)
		if count == 0 then
			display (n1)
		else if count = 1 then
			display (n2)
		else
			n3 = n1 + n2
			display (n3)
			n1 = n2
			n2 = n3
try
	n = convert_to_integer(input (“Enter your number: ”))
except
	display (“Invalid input.”)
else
	Fibonacci(n)
