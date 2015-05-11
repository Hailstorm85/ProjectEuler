from timer import Timer
import math

with Timer() as t:
	def isPrime(n):
		'''check if integer n is a prime'''
		# make sure n is a positive integer
		n = abs(int(n))
		# 0 and 1 are not primes
		if n < 2:
			return False
		# 2 is the only even prime number
		if n == 2: 
			return True    
		# all other even numbers are not primes
		if not n & 1: 
			return False
		# range starts with 3 and only needs to go up the squareroot of n
		# for all odd numbers
		for x in range(3, int(n**0.5)+1, 2):
			if n % x == 0:
				return False
		return True
	i = 0
	j = 2
	list = []
	while i < 100001:
		if isPrime(j):
			list.append(j)
			i += 1
		j += 1
	print list[i-1]
print "Executed time = %s s" %t.secs