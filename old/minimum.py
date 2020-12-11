def minimum(lst):
	"""
	parameters : lst of type list
	return : the value of the smallest element in the lst
	"""
	if len(lst) == 1:
		return lst[0]

	if lst[0] < lst[1]:
		lst.append(lst[0])
		return(minimum(lst[1:]))
	return(minimum(lst[1:]))

# acc, the accumulator, represents the current lowest found
# def my_minimum(lst, acc = None):
#    if not lst: # If the list is empty, return the current lowest
#       return acc

#    # Head is the first element, and the tail is the rest of the list
#    # This is a common pattern when recursively iterating a list
#    # head, tail = lst[0], lst[1:]
#    head, *tail = lst

#    # The first time this is run, "not acc" fails, and it defaults to head
#    new_acc = head if not acc or head < acc else acc

#    return my_minimum(tail, new_acc)

# lst = [2, 3, 4, 9, 2, -2]

# print(my_minimum(lst))

# def minimum(lst):

#     if len(lst)==1:
#         return lst[0]

#     if lst[0] < lst[1]:
#         return minimum(lst[0:1] + lst[2:])
#     else:
#         return minimum(lst[1:])

lst = [2, 3, 4, 9, 2, -2]

print(minimum(lst))