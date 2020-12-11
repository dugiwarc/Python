
# def changer(element, lst[0][0]):
# 	if lst[0][0]==1:
# 		print("changed")
# 		return changer(element, lst[0][1])


# l = [0,0,0,1,1,0,0]

import Labyrinthe
l = Labyrinthe.creer(5,5)

# def change(element, lst):
# 	if not lst:
# 		return lst
# 	if lst[0]==element:
# 		lst[0]=0
# 		print("yay")
# 		return change(element,lst[1:])
# 	print("nay")
# 	return change(element,lst[1:])

# change(1, l)

# print(l)

def f(element, lst):
	if not lst:
		return 0
	if len(lst[0])==0:
		return f(element,lst[1:])
	if lst[0][0]==2:
		print("yay")
		return f(element,lst[0][1:])
	return f(element, lst[0][1:])

f(2, l)