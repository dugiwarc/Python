def sum_pairs(ints, s):
	"""
	parameters: a list ints;
				a number s;
	returns: the first pair of the numbers whose sum
			 equals the number passed to the function
	"""
	already_visited = set()
	for i in ints:
		difference = s - i
		if difference in already_visited:
			return [difference, i]
		already_visited.add(i)
	return []
