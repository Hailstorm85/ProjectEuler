import math

n = int(raw_input("? "))
listPrime = []
lastFactor = 1
if n % 2 == 0:
	lastFactor = 2
	while n % 2 == 0:
		listPrime.append(2)
		n //= 2

factor = 3

maxFactor = math.sqrt(n)
while n > 1 and factor <= maxFactor:
	while n % factor == 0:
		lastFactor = factor
		listPrime.append(factor)
		n //= factor
	factor += 2

if n == 1:
	print listPrime
	print lastFactor
else:
	listPrime.append(n)
	print listPrime
	print n
	