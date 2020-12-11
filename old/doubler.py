def double(lst):
	"""
	parameters : lst of type list;
	returns : lst with its elements doubled
	"""
	if not lst:
		return []
	return [2 * lst[0]] + double(lst[1:]) # [2*lst[0]] + double(lst[1:])

print(double([1,2,3,4,5,6,7,8]))