def somme_premiers_entiers(n):
	'''
	parametres : un entier n;
	resultat : un entier
	pre-conditions : n >= 0
	'''
	if n == 0:
		return 0
	else:
		print(n)
		return somme_premiers_entiers(n - 1) + n

print(somme_premiers_entiers(10))