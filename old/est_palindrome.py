def is_Pal(txt):
	"""
	parameter : txt of type string;
	returns   : True if txt is a palindrome and False if not;
	"""
	if len(txt)==0:
		return True
	if txt[0]!=txt[-1]:
		return False
	return is_Pal(txt[1:-1])

print(is_Pal("gepotkopeg"))
