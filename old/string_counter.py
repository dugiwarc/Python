def counter(z, c = 0):
	"""
	parameters : z of type string
	returns : the number of characters that the string holds
	"""
    if z == "": 
        return c
    else:
        return counter(z[1:], c + 1)

print(counter("hello"))