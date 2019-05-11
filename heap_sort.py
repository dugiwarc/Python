def heapify(arr, n, i):
	"""
	Python program for implementation of heap Sort
	To heapify subtree rooted at index i.
	n is size of heap
	"""

	largest = i    # initialize largest as root
	l = 2 * i + 1  # left = 2 * i + 1
	r = 2 * i + 2  # right ...

	#See if left child of roots exists and is greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	#See if right child of roots exists and is greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	#Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		heapify(arr, n, largest)

def heapSort(arr):
	n - len(arr)

	#Build a maxheap
	for i in range(n, -1, -1):
		heapify(arr, n, i)

	