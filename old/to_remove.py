def shellSort(input):
	gap = len(input) / 2
	while gap > 2:
		for i in range(gap, len(input)):
			temp = input[i]
			j = i

			while j >= gap and input[j - gap] > temp:
				input[j] = input[j - gap]
				j = j - gap
			input[j] = temp

		gap = gap/2

lst = [19,2,31,45,30,11,121,27]

print(shellSort(lst))
