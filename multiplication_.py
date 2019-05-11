def mult(a, b):
	'''
	parametres : deux entiers a et b
	resultat : un entier
	pre-conditions : b >= 0
	'''
	if b == 0:
		return 0
	else:
		print(a,b)
		return mult(a, b - 1) + a

print(mult(4, 5))
