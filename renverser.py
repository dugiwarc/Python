def reverse(lst):
	"""
	parameters : lst of type list
	returns : another lists with the elements positioned in a reversed order
	"""
	if lst == []:
		return []
	else:
		return [lst[-1]] + reverse(lst[:-1])

print(reverse([1,2,3,4,5,6]))