from timer import Timer
import math

with Timer() as t:
	
	def eratosthenes(n):
		multiples = []
		for i in range(2, n+1):
			if i not in multiples:
				print (i),
				for j in range(i*i, n+1, i):
					multiples.append(j)

	eratosthenes(10000)
	print
	
print "Executed time = %s s" %t.secs