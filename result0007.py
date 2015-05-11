from timer import Timer
import math

with Timer() as t:
	def isPrime(n):	
		if n < 2:
			return False
		elif n < 4:
			return True
		elif n % 2 == 0:
			return False
		elif n < 9:
			return True
		elif n % 3 == 0:
			return False
		else:
			r = math.sqrt(n)
			f = 5
			while f <= r:
				if n % f == 0:
					return False
				if n % (f+2) == 0:
					return False
				f = f + 6
			return True
	
	limit = 100001
	count = 1
	candidate = -10
	while count < limit:
		candidate += 2
		if isPrime(candidate):
			count += 1
	print candidate
		
print "Executed time = %s s" %t.secs