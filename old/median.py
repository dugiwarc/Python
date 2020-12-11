
summ=0
c=0
result=0
a = ''
a = str(input("enter your name"))
while(a):
	a = str(input("Subject: "))
	
	if str(a) == "math":
		grade = float(input("Estimated grade: "))
		summ += grade*0.6
		print(summ)

	elif a == "cpi":
		grade = float(input("Estimated grade: "))
		summ += grade*0.3
		print(summ)


	elif a == "mtu":
		grade = float(input("Estimated grade: "))
		summ += grade*0.2
		print(summ)

	elif a == "analyse":
		grade = float(input("Estimated grade: "))
		summ += grade*0.3
		print(summ)

	elif a == "algebre":
		grade = float(input("Estimated grade: "))
		summ += grade*0.4
		print(summ)

	elif a == "bai":
		grade = float(input("Estimated grade: "))
		summ += grade*0.3
		print(summ)

	elif a == "algo":
		grade = float(input("Estimated grade: "))
		summ += grade*0.6
		print(summ)

	elif a == "eng":
		grade = float(input("Estimated grade: "))
		summ += grade*0.3
		print(summ)

Median = float(summ) / float(30)