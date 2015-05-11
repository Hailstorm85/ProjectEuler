from timer import Timer
import math

with Timer() as t:
	limit = 50000
	for a in xrange(3, (limit - 3) // 3):
		for b in xrange(a + 1, (limit - 1 - a) // 2):
			c = limit - a - b		
			if a * a + b * b == c * c:
				print a, b, c, a * b * c

print "Executed time = %s s" %t.secs