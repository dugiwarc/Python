def wovel_count(string):
	"""
	parameters: a string 
	returns: a dictionary with the keys as the vowels
			 and values as the count of time that vowel
			 appears in the string
	"""
	lower_s = string.lower()
	# count the vowels in the 
	return {letter: lower_s.count(letter) for letter in string if letter in "aeiou"}

print(wovel_count("afasgaasg"))