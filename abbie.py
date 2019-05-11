import TP5
import Labyrinthe
laby=Labyrinthe.creer(15,15)

def createFile():
	tailleCube=20
	hauteur=len(laby)*tailleCube
	largeur=len(laby)*tailleCube
	f=open("Labyrinthe.pgm","w")
	f.write("P2 \n"+str(hauteur)+" "+str(largeur)+"\n255\n")

	
	for y in range(hauteur):
		for x in range(largeur):
				indx=x//tailleCube
				indy=y//tailleCube
				a=laby[indy][indx] 
				if(a==0):
					f.write("0 ")
				if(a==1):
					f.write("255 ")
				if(a==3):
					f.write("127 ")
				if(a==2):
					f.write("128 ")
	f.close()

createFile()			
def estAcc(f,lst):
	(lgn,col)=f
	if(lst[lgn][col]!=0):
		return True
	else :
		return False
	


def explore(f,lst,exp):
	(l,c)=f
	if lst[l][c]==3:
		return exp +[(l,c)]