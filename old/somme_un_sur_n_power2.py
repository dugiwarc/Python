from multiplication_ import mult

def somme_un_sur_power2(n):
	'''
	parametres : un entier n;
	resultat : un flottant
	pre-conditions : n >= 1
	'''
	if n == 1:
		return 1.0
	else:
		print(n)
		return 1.0/(mult(n,n)) + somme_un_sur_power2(n - 1)

print(somme_un_sur_power2(4))