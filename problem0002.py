a, fib = 1, 1
sum = 0
target = 4000000

def SumIfEven(number, sum):
	return sum + number if number % 2 == 0 else sum

while fib < target:
	fib, a = fib + a, fib
	sum = SumIfEven(fib, sum)

print sum