def titleize(string):
	"""
	parameters : a string of words
	returns : a new string with the first
			  letter in every string capitalized
	"""
	return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))
