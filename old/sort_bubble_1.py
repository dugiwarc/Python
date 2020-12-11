lst=[1,2,3,4,5,9]

x=5

a=False
n=len(lst)
for i in range(0, n-1):
	if lst[i] == x:
		a=True
print("Le resultat est la valeur de", a)