
def triSelection(a):
"""
Principe: On determine la position du plus petit element, on le met
			en premier position(en echangeant avec le premier element),
			et on itere le procede sur le tableau restant.
Complexite: O(n^2) dans tous le cas
"""
	n = len(a)
	for i in range(n):
		k = i
		for j in range(i + 1, n):
			if a[k] > a[j]:
				a[k], a[i] = a[i], a[k]

print(triSelection([1,3,2,5,7,6,0]))

