def count_even(lst, c = []):
	"""
	parameters : a lst of type list
	returns : the even elements from that list
	"""
	if lst == []:
		return c
	if lst[0] % 2 == 0:
		c += [lst[0]]
	return count_even(lst[1:], c)



print(count_even([1,2,3,4,5,6,7,8,9]))