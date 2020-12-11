def est_pair(n):
	"""
	parametres : un entier n;
	resultat : un booleen
	pre-conditions : n >= 0
	"""
	if n == 0:
		return True
	elif n == 1:
		return False
	else:
		return est_pair(n - 2)

print(est_pair(123))