
def est_premier(n, x = 2):
	if n == x:
		return True
	if n % x == 0:
		return False
	return est_premier(n, x + 1) 
print(est_premier(59))