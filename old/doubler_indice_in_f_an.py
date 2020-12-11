def double_index_less_than_n(lst, n, c = -1):
	"""
	parameters : lst of type list;
				 n of type int;
	returns : returns the same list, with all 
			  the elements up to index n multiplied by 2
	""" 
	if c == n:
		return [] + lst
	else:
		return [lst[0] * 2] + double_index_less_than_n(lst[1:], n, c + 1)

print(double_index_less_than_n([1,2,3,4,5,6], 3))