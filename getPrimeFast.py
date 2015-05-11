from timer import Timer
import math

with Timer() as t:
	"""
	def get_primes(n):
		numbers = set(range(n, 1, -1))
		primes = []
		while numbers:
			p = numbers.pop()
			primes.append(p)
			numbers.difference_update(set(range(p*2, n+1, p)))
		return primes
	"""
	def get_primes(n):
		""" Returns  a list of primes < n """
		sieve = [True] * n
		for i in xrange(3,int(n**0.5)+1,2):
			if sieve[i]:
				sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
		return [2] + [i for i in xrange(3,n,2) if sieve[i]]
	
	print get_primes(1000000)
print "Executed time = %s s" %t.secs