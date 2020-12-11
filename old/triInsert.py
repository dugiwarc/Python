def triInstertion(lst):

	n = len(lst)

	for i in range(1, n):

		key = lst[i]

		# On va deplacer les elements de lst[0..i-1], qui sont plus
		#   grands que key, a une position d'avance 
		j = i - 1
		while j >= 0 and key < lst[j]:
			lst[j+1] = lst[j]
			j -= 1
		lst[j+1] = key
	return lst


print(triInstertion([1,3,5,6,8,2,4,7]))