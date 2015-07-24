from timer import Timer
from sys import argv
import math
import fractions

limit = int(argv[1])
with Timer() as t:
	for a in xrange(3, (limit - 3) // 3):
		for b in xrange(a + 1, (limit - 1 - a) // 2):
			c = limit - a - b		
			if a * a + b * b == c * c:
				print a, b, c, a * b * c
time1 = t.secs
				
with Timer() as s:
	lim2 = limit // 2
	mlimit = int(math.ceil(math.sqrt(lim2))) - 1
	for a in xrange(2, mlimit):
		if lim2 % a == 0:
			b = lim2 // a
			while b % 2 == 0:
				b = b // 2
			if a % 2 == 1:
				k = a + 2
			else:
				k = a + 1
			while k < 2 * a and k <= b:
				if b % k == 0 and fractions.gcd(k, a) == 1:
					d = lim2 // (k * a)
					n = k - a
					t = d * (a * a - n * n)
					u = 2 * d * a * n
					v = d * (a  * a + n * n)
					print t, u ,v, t * u * v
				k += 2
time2 = s.secs

print "Executed time = %s s" %time1
print "Executed time = %s s" %time2