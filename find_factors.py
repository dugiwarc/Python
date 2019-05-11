def find_factors(num):
	"""
	parameters: a number
	returns: a list of all of the numbers which are divisible
			 by starting from 1 and going up the number
	"""
	factors = []
	i = 1
	while i <= num:
		if num % i == 0:
			factors.append(i)
		i += 1
	return factors
print(find_factors(100))