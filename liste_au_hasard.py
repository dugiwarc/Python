import random

def random_list(n, valmax, lst = []):
	"""
	parameters : n of type int;
			     valmax of type int;
	returns    : a list of n numbers picked randomly from the interval 
				 [0, valmax]
	"""
	if n == 0:
		return []
	return [random.randint(0, valmax)] + random_list(n-1, valmax)

print(random_list(10, 100))
	