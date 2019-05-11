A = [64, 25, 12, 22, 11]

def sorted(array):
	# Traverse through all aray elements
	for i in range(len(A)):
		# Find the minimum element in remaining unsorted array
		min_idx = i
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j

		A[i], A[min_idx] = A[min_idx], A[i]

	print("Sorted array")
	for i in range(len(A)):
		print("%d" %A[i], end="")
sorted(A)