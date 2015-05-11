from timer import Timer
import math
import fractions 

with Timer() as s:
	limit = 5000000
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
					print t, u ,v
				k += 2

print "Executed time = %s s" %s.secs