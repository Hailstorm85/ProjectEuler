import math

listPrime = []
i = 2
n = 100

while i*i <= n and n > 1:
	while n % i == 0:
		listPrime.append(i)
		n /= i
	i += 1

if n > 1:
	listPrime.append(int(n))
	
print listPrime
print i
