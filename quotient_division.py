def quotientDivision(n, b, q = 0):
	"""
	parameters : a et b (integers)
	returns: the remainder of a and b
	"""
	if n < b:
		return n, q
	else:
		return quotientDivision(n - b, b, q + 1)

print(quotientDivision(274,5))