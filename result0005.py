from timer import Timer
import math

with Timer() as t:
	
	def listPrime(n):
		numbers = set(range(n, 1, -1))
		primes = []
		while numbers:
			p = numbers.pop()
			primes.append(p)
			numbers.difference_update(set(range(p*2, n+1, p)))
		return primes

	k = 20
	result = 1
	i = 1
	str = ""
	limit = math.sqrt(k)
	p = listPrime(k)
	print p
	
	for i in range(0, len(p)):
		if p[i] <= limit:
			a = math.log(k) // math.log(p[i])
		else:
			a = 1
		result = result * math.pow(p[i], a)
		if i == 0:
			str = str + "%s ^ %.0f" %(p[i], a) 
		else:
			str = str + " * %s ^ %.0f" %(p[i], a) 
	print result
	print str
		
print "Executed time = %.6f s" %t.secs
