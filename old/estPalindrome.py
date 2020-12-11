def rem_spaces(string, g=''):
	"""
	parameters : string of type str;
	returns : a string with all the spaces removed
	"""

	if len(string)==0:
		return g
	if string[0]!=' ':

		return rem_spaces(string[1:], g+string[0])
	return rem_spaces(string[1:], g)

def isPalindrome(string):
	"""
	parameters : string of type str
	returns : True if the string is a palindrome, False if not
	"""
	string=rem_spaces(string)
	if len(string) % 2 != 0:
		return False
	if len(string)==0:
		return True
	if string[0]==string[-1]:
		return isPalindrome(string[1:-1])
	return isPalindrome(string[1:-1])


print(isPalindrome('ferdihe            '))