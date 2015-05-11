from timer import Timer
import math

with Timer() as t:
	
	def getPrime(number):
		prime = [2]
		
		for n in range(3, number):			
			checkPrime = True
			i = 2
			while i * i <= n:
				if n % i == 0:
					checkPrime = False
				i += 1					
			if checkPrime == True:
				prime.append(n),
		return prime
	print getPrime(100000)
print "Executed time = %s s" %t.secs		