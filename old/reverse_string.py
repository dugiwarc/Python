def reverse_string(string):
	s = ''
	for i, char in enumerate(string[::-1]):
		s += char
	return s 