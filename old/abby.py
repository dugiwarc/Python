import Labyrinthe

laby= Labyrinthe.creer(11,15)
# ~ for i in laby:
	# ~ print(i)
	
def entree(lst):
	
	for (i,e) in enumerate(laby):
		for (ind,elem) in enumerate(laby[i]):
			if(elem==2):
				return (ind , i)

def sortie(lst):
	
	for (i,e) in enumerate(laby):
		for (ind,elem) in enumerate(laby[i]):
			if(elem==3):
				return (ind , i)
				
def taille(lst):
	for (i,e) in enumerate(lst):
		for (ind,elem) in enumerate(lst[i]):
			a=(i+1, ind+1)
			
	return a
		
def nbLignes(lst):
	for (i,e) in enumerate(lst):
		a= (i)
	
	return a
		
def nbColonnes(lst):
	for (i,e) in enumerate(lst):
		for (ind,elem) in enumerate(lst[i]):
			a=(ind)
	
	return a
	
def voisin_laby(f,lst):
	(lgn,col)=f
	l=[]
	
	if (lgn != 0):
		l +=[(lgn-1,col)]
	
	if(lgn != nbLignes):
		l+=[(lgn+1,col)]
		
	
	if(col != 0):	
		l +=[(lgn,col-1)]
	
	if(col != nbColonnes):
		l+=[(lgn,col+1)]
	else:
		l+=[]
		
	
	# ~return "voisinDroite= ",voisinDroite,"voisinGauche= ",voisinGauche,"voisinDessus= ",voisinDessus,"voisinDessous= ",voisinDessous,l
	return l
	
def voisin_laby_final(f,lst):
	(lgn,col)=f
	if(lgn==0):
		voisinDessus="pas de voisin dessus"
	else:
		voisinDessus=(lst[lgn-1][col])
	if(lgn==nbLignes(lst)):
		voisinDessous="pas de voisin dessous"
	else:
		voisinDessous=(lst[lgn+1][col])
		
	if(col==0):
		voisinGauche="pas de voisin Gauche"
	else:	
		voisinGauche=(lst[lgn][col-1])
	if(col==nbColonnes(lst)):
		voisinDroite="pas de voisin droite"
	else:
		voisinDroite=(lst[lgn][col+1])
		
	l=[voisinDessus,voisinDessous,voisinDroite,voisinGauche]
	# ~return "voisinDroite= ",voisinDroite,"voisinGauche= ",voisinGauche,"voisinDessus= ",voisinDessus,"voisinDessous= ",voisinDessous,l
	return l

def voisin_laby_acc(f,lst):
	(lgn, col)=f
	voisins=voisin_laby(f,lst)
	l=[]
	for (i,e) in enumerate(voisins):
		(lgn,col)= voisins[i]
		if(lst[lgn][col] !=0 and lst[lgn][col]!=4):
			l += [voisins[i]]
			
		
		
	return l
	
# ~ print(position((5,5),laby))			
# ~ print(entree(laby))
# ~ print(sortie(laby))
# ~ print(taille(laby))
# ~ print(nbLignes(laby))
# ~ print(nbColonnes(laby))
# ~ print(voisin_laby(0,0,laby))
# ~ print(voisin_laby(nbLignes(laby),nbColonnes(laby),laby))
# ~ print(voisin_laby(nbLignes(laby),0,laby))
# ~ print(voisin_laby((1,1),laby))
# ~ print(voisin_laby((2,2),laby))
# ~ print(voisin_laby_final((0,0),laby))
# ~ print(voisin_laby_acc((1,1),laby))
print(99999%100)
			
			
def test12():
	lst1 = []
	for i in range(3):
		for j in range(4):
			
			lst1[i][j] += [i+1]
	return lst1
	
# ~ print(test12())
	