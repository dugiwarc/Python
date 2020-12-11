def suite_geom(n, u0, r):
	'''
	parametres : un entier n (indice);
				 un flottant u0 (le premier terme);
				 un flottant r (la raison de la suite);
	resultat : un entier
	pre-conditions : n >= 0
	'''
	if n == 1:
		return u0
	else:
		# print(suite_geom(n, u0, r))
		return suite_geom(n - 1, u0, r) * r

print(suite_geom(4, 1, 9))