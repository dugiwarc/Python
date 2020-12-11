def indice(lst, to_find, c = 0):
	"""
	parameters : lst of type list
				 to_find of type int
	return : the index of to_find in lst
	""" 
	if lst == []:
		return -1
	if to_find == lst[0]:
		return c
	else:
		return indice(lst[1:], to_find, c + 1)

print(indice([1,2,3,-3,5,6,7],-3))