def triSelect(lst):
	n = len(lst)
	b = lst
	for i in range(0,n):
		for j in range(1+i, n):
			if lst[i]>lst[j]:
				lst[i],lst[j] = b[j],b[i]

	return b

print(triSelect([4,2,6,3,8,5,7,9,1,0]))

