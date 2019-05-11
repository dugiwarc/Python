def merge_sort(unsorted_list):
	if len(unsorted_list) <= 1:
		return unsorted_list

	# Find the middle point and divide it
	middle = len(unsorted_list) // 2
	left_list = unsorted_list[:middle]
	print(left_list)
	right_list = unsorted_list[middle:]
	print(right_list)

	left_list = merge_sort(left_list)
	right_list = merge_sort(right_list)
	return list(merge(left_list, right_list))

def merge(left_half, right_half):
	print("on")
	res = []
	while len(left_half) != 0 and len(right_half) != 0:
		print(left_half, right_half)
		if left_half[0] < right_half[0]:
			res.append(left_half[0])
			print("res",res)
			left_half.remove(left_half[0])
		else:
			res.append(right_half[0])
			print("res",res)
			right_half.remove(right_half[0])
	if len(left_half) == 0:
		res = res + right_half
	else:
		res = res + left_half
	return res


print(merge_sort([33,423,52,736,300,430,643,739]))