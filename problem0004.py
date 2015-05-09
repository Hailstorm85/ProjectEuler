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
	limit = 1000
	maxPalin = 0
	
	for i in range(start, limit):
		for j in range(i, limit):
			number = i * j
			if checkPalindrome(number) and maxPalin < number:
				maxPalin = number
				a, b = i, j
			
	print a, b, maxPalin
print "time = %s s" %t.secs
