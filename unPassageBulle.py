def unPassageBulle(lst):
	n = len(lst)

	for i in range(0, n):
		for j in range(i+1, n):
			if lst[i]>lst[j]:
				lst[i],lst[j] = lst[j], lst[i]

	return lst

print(unPassageBulle([1,2,3,5,4,6,7,8]))