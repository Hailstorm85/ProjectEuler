from timer import Timer
import math

with Timer() as t:

	def sumOfSquare(n):
		sum = (2 * n + 1) * (n + 1) * n / 6
		return sum

	def squareOfSum(n):
		sum = n * (n + 1) / 2
		return sum * sum
	
	limit = 10000000
	
	diff = squareOfSum(limit) - sumOfSquare(limit)
	print diff
	
print "Executed time = %s s" %t.secs