from multiplication_ import mult

def mult_neg(a, b):
	'''
	parametres : deux entiers a et b
	resultat : un entier
	pre-conditions :
	'''
	if b == 1:
		return mult(a ,b)
	else:
		return mult(-a, -b)

# print(mult(-4, 3))