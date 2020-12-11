def diviseur(n, p):
	'''
	parametres : un entier n et un entier p
	resultat : la verite si n a p comme diviseur 
	pre-conditions : p <= 1
	'''
	if p < 0:
		return False
	return diviseur(n, p - n) or (p == 0)

print(diviseur(4,20))