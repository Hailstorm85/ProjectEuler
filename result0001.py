def SumByDivisible(number, range):
	p = range // number
	return number * p * (p+1) // 2 

target = int(raw_input("target?")) - 1
	
print SumByDivisible(3, target) + SumByDivisible(5, target) - SumByDivisible(15, target)
	