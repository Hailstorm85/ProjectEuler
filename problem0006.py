from timer import Timer
import math

with Timer() as t:

	def sumOfSquare(n):
		sum = 0
		for i in xrange(1, n+1):
			sum += i * i
		return sum

	def squareOfSum(n):
		sum = 0
		for i in xrange(1, n+1):
			sum += i
		return sum * sum
	
	limit = 1000

	diff = squareOfSum(limit) - sumOfSquare(limit)
	print diff
	
print "Executed time = %.6f s" %t.secs