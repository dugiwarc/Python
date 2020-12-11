def chemin(lst, x):
	if x == lst[0]:
		return 0
	return chemin(lst[1:], x) + 1
	
print(chemin([1,2,3,4,5], 4))