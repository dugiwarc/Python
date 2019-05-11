def listeNulle(n, c = 0, m = []):
	"""
	parameters : n of type int
	returns : a list with a count of n zeros
	notes : avoid using the operator "*"
	""" 
	if len(m) == n:
		return m
	else:
		m += [int(0)] 
		return listeNulle(n, c + 1)

print(listeNulle(8))