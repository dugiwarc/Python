def delete(lst, to_delete):
	"""
	parameters : lst of type list
				 to_delete : represents a value one wants to delete from the list
	returns : another list with the same elements minus the ones one asks to delete
	"""
	if not lst:
		return []
	else:
		if lst[0] == to_delete:
			return delete(lst[1:], to_delete)
		return [lst[0]] + delete(lst[1:], to_delete)

print(delete([1,2,3,4,5,5,6,5,7,5], 5))