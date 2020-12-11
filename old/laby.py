import Labyrinthe
l = Labyrinthe.creer(19,19)

def findElement(element, l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if element==l[i][j] and ((l[i-1][j] == 2) or (l[i+1][j] == 2) or (l[i][j-1] == 2) or (l[i][j+1] == 2)):
            	l[i][j] = 2
            	findElement(element, l)
    l[1][1] = 8           
    return None

def clearPath(element, l):
	for i in range(len(l)):
		for j in range(len(l[i])):
			if element == l[i][j] and (l[i-1][j] + l[i+1][j] + l[i][j-1] + l[i][j+1] <= 2):
				l[i][j] = 0
				clearPath(element, l)

def painter(l,file):
	file = input("Name of the solution file\n")
	size = 20  #size of a tile in pixels
	rows = len(l)
	columns = len(l[0])
	height = size * rows 
	width = size * columns

	f = open(file, "w")
	f.write("P2\n" + str(width) + " " + str(height) + "\n255\n") 

	for y in range(height):
		for x in range(width):
			indx = x // size
			indy = y // size
			a = l[indy][indx]
			if a == 0:
				f.write(str(50) + " ")   # colors the pixels
			elif a == 2:
				f.write(str(100) + " ")
			elif a == 3:
				f.write(str(170) + " ")
			else:
				f.write(str(a) + " ")
	f.close()

findElement(1, l)
for i in l:
	print(i)
painter(l, "")
print("="*30)
print(" "*30)
print("="*30)
clearPath(2, l)
painter(l, "")
for i in l:
	print(i)
