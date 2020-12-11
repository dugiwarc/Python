def suite_arith(n,u0,r):
	'''
	parametres : un entier n (indice)
				 un flottant u0 (le premier terme)
				 un flottant r (la raison de la suite)
	resultat : un entier
	pre-conditions : n >= 0
	'''
	if n == 0:
		return u0
	else:
		print(n, u0, r)
		return suite_arith(n-1, u0, r) + r

print(suite_arith(2,0,3))