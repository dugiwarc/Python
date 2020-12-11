def permute(lst, i, j):
	
	lst[i], lst[j] = lst[j], lst[i]
	print(lst)

	return None

print(permute([1,2,3,4,5,6],0,4))