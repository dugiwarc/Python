def afficher_n_fois(n, message):
	"""
	parametres : un entier n;  un string message;
	resultat : none
	pre-conditions: n >= 0
	"""
	if n >= 1:
		print(message)
		afficher_n_fois(n - 1, message)

afficher_n_fois(5, "Error")