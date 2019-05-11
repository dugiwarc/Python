def min(lst, x=100):
	for i in lst:
		if i < x:
			x = i
	print(x);

min([2,3,6,4,1,6,7,0])

def sort(lst):
	for i in range(len(lst)):
		for j in range(i+1, len(lst)):
			if lst[i] > lst[j]:
				lst[i], lst[j]=lst[j],lst[i]
				print(lst)

	print(lst)

	
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list)