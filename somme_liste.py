def sumList(n, sum = 0):
	"""
	parameters : a list
	returns : the sum of the list's elements
	"""
	if n == []:
		return sum
	else:
		print(n)
		return sumList(n[1:], sum + n[0])

print(sumList([3,5,6,5,7,2,3,6,-2,-3,2.4]))