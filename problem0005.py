from timer import Timer

with Timer() as t:
	
	def checkDivisible(num):
		for i in range(1, 20):
			if num % i != 0:
				return False
		return True
	
	number = 1
	while not checkDivisible(number):
		number += 1
	
	print number
	
print "Executed time = %.6f s" %t.secs