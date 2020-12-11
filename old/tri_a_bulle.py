def triBulle(a):
	"""
	Principe   : Consiste a comparer, en commencant par la fin de la liste
					les couples d'elements succesifs. Lorsque deux elements successifs ne sont pas 
					pas dans l'ordre croissant, ils sont echanges. On fait ainsi remonter le terme 
					le plus petit.Puis on itere le procede sur le sous-tableau restant:

	Complexite : O(n^2)
	"""
	n = len(a)
	for i in range(n-1):
		for j in range(n-1,i,-1):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
	return a

print(triBulle([1,3,2,5,7,6,0]))
