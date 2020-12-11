import Labyrinthe
l = Labyrinthe.creer(7,7)
for i in l:
	print(i)

def buildPath(element, l):
	if element==l[i][j] and ((l[i-1][j] == 2) or (l[i+1][j] == 2) or (l[i][j-1] == 2) or (l[i][j+1] == 2)):
        l[i][j] = 2
            buildPath(element, l)
    l[1][1] = 8           
    return None

def clearPath(element, l):
	for i in range(len(l)):
		for j in range(len(l[i])):
			if element == l[i][j] and (l[i-1][j] + l[i+1][j] + l[i][j-1] + l[i][j+1] <= 2):
				l[i][j] = 0
				clearPath(element, l)


buildPath(1, l)
clearPath(2, l)

print("\n")
for i in l:
	print(i)

