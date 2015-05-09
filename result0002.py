fib1, fib2, fib3 = 1, 1, 2
sum = 0
limit = 4000000

while fib3 < limit:
	sum = sum + fib3
	fib1 = fib2 + fib3
	fib2 = fib3 + fib1
	fib3 = fib1 + fib2

print sum