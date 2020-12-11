def remainderDivision(n, b):
	"""
	parameters : a et b (integers)
	returns: the remainder of a and b
	"""
	if n < b:
		return n
	else:
		return remainderDivision(n - b, b)

print(remainderDivision(-274,5))