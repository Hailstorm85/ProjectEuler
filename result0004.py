from timer import Timer

with Timer() as t:
	
	def reverseNumber(num):
		rev = 0
		while num > 0:
			rev = 10 * rev + num % 10
			num //= 10
		return rev
		
	def checkPalindrome(number):
		return number == reverseNumber(number)
		
	start = 100
	maxPalin = 0
	i = 999
	
	while i >= start:
		
		if i % 11 == 0:
			j = 999
			db = 1
		else:
			j = 990
			db = 11		
			
		while j >= i:
			number = i * j
			if number < maxPalin:
				break						
			if checkPalindrome(number) and maxPalin < number:
				maxPalin = number
				a, b = i, j
			j -= db
			
		i -= 1
	
	print a, b, maxPalin
	
print "Executed time = %.6f s" %t.secs